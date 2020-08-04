from datetime import datetime
from django.core.paginator import PageNotAnInteger, EmptyPage
from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from pygments import highlight
from pygments.formatters import get_formatter_by_name
from pygments.lexers import get_lexer_by_name
from taggit.models import TaggedItemBase
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel
from wagtail.core.blocks import TextBlock, StructBlock, StreamBlock, CharBlock, RichTextBlock, \
    ChoiceBlock
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core.models import Page
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet

from lib.ellipsis_paginator import EllipsisPaginator

@register_snippet
class Footer(models.Model):
    facebook_url = models.URLField(null=True, blank=True)
    twitch_url = models.URLField(null=True, blank=True)
    twitter_url = models.URLField(null=True, blank=True)
    privacy_policy_url = models.URLField(null=True, blank=True)

    panels = [
        FieldPanel('facebook_url'),
        FieldPanel('twitch_url'),
        FieldPanel('twitter_url'),
        FieldPanel('privacy_policy_url'),
    ]

    def __str__(self):
        return 'Footer URLs'


@register_snippet
class SocialMedia(models.Model):
    url = models.URLField()
    icon = models.CharField(max_length=30)
    name = models.CharField(max_length=30)

    panels = [
        FieldPanel('name'),
        FieldPanel('url'),
        FieldPanel('icon'),
    ]

    def __str__(self):
        return self.name


@register_snippet
class Sponsor(models.Model):
    class TIERS(models.IntegerChoices):
        LAPSED = 0, "Lapsed (Not shown anywhere)"
        BRONZE = 1, "Bronze (Appears in sponsor page)"
        SILVER = 2, "Silver (Appears in sponsors and homepage)"
        GOLD = 3, "Gold (Appears on every page)"

    sponsor_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='This image will be displayed in all sponsor display locations across the website'
    )
    nightmode_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='This image will be displayed in all sponsor display locations across the website in night mode'
    )
    url = models.URLField(null=True, blank=True)
    name = models.CharField(max_length=255)
    email_sponsor = models.BooleanField(default=True, help_text='Should this sponsor be included in the newsletters?')
    email_text_markdown = models.TextField(blank=True, max_length=4000,
                                           help_text='The text content in our newsletter emails. Is required to be valid markdown',
                                           verbose_name='Email text')
    tier = models.IntegerField(default=1, choices=TIERS.choices)

    panels = [
        MultiFieldPanel([
            FieldPanel('name'),
            FieldPanel('tier'),
            FieldPanel('url'),
            ImageChooserPanel('sponsor_image'),
            ImageChooserPanel('nightmode_image'),
        ], heading='Sponsor information'),
        MultiFieldPanel([
            FieldPanel('email_sponsor'),
            FieldPanel('email_text_markdown')
        ], heading='Email content')
    ]

    def __str__(self):
        tier = self.TIERS(self.tier).name.capitalize()
        if self.email_sponsor:
            tier += '+Email'
        return self.name+" ("+tier+")"


class PullQuoteBlock(StructBlock):
    quote = TextBlock("quote title")
    attribution = CharBlock()

    class Meta:
        icon = "openquote"


class Heading2Block(CharBlock):
    class Meta:
        template = 'blog/blocks/h2.html'


class Heading3Block(CharBlock):
    class Meta:
        template = 'blog/blocks/h3.html'


class Heading4Block(CharBlock):
    class Meta:
        template = 'blog/blocks/h4.html'


class CodeBlock(StructBlock):
    """
    Code Highlighting Block
    """
    LANGUAGE_CHOICES = (
        ('bash', 'Bash/Shell'),
        ('c', 'C'),
        ('cmake', 'CMake'),
        ('cpp', 'C++'),
        ('csharp', 'C#'),
        ('css', 'CSS'),
        ('go', 'Go'),
        ('haskell', 'Haskell'),
        ('haxe', 'Haxe'),
        ('html', 'HTML'),
        ('java', 'Java'),
        ('js', 'JavaScript'),
        ('json', 'JSON'),
        ('kotlin', 'Kotlin'),
        ('lua', 'Lua'),
        ('make', 'Makefile'),
        ('perl', 'Perl'),
        ('perl6', 'Perl 6'),
        ('php', 'PHP'),
        ('python', 'Python'),
        ('python3', 'Python 3'),
        ('ruby', 'Ruby'),
        ('sql', 'SQL'),
        ('swift', 'Swift'),
        ('xml', 'XML'),
    )

    language = ChoiceBlock(choices=LANGUAGE_CHOICES)
    code = TextBlock()

    class Meta:
        icon = 'code'

    def render(self, value, **kwargs):
        src = value['code'].strip('\n')
        lang = value['language']

        lexer = get_lexer_by_name(lang)
        formatter = get_formatter_by_name(
            'html',
            linenos='inline',
            cssclass='code-highlight',
            style='default',
            noclasses=False,
        )
        return mark_safe(highlight(src, lexer, formatter))


class BlogStreamBlock(StreamBlock):
    h2 = Heading2Block(icon="title", classname="title")
    h3 = Heading3Block(icon="title", classname="title")
    h4 = Heading4Block(icon="title", classname="title")
    paragraph = RichTextBlock(icon="pilcrow")
    image = ImageChooserBlock()
    pullquote = PullQuoteBlock()
    document = DocumentChooserBlock(icon="doc-full-inverse")
    code = CodeBlock()


class HomePage(Page):
    # Parent page/subpage rules
    subpage_types = ['blog.BlogIndexPage', 'blog.AboutPage', 'events.EventsIndexPage']

    description = StreamField(BlogStreamBlock())
    alert = RichTextField(blank=True, features=['bold', 'italic'])
    alert_link = models.URLField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('alert'),
        FieldPanel('alert_link'),
        StreamFieldPanel('description'),
    ]


class BlogIndexPage(Page):
    # Parent page/subpage rules
    parent_page_types = ['blog.HomePage']
    subpage_types = ['blog.BlogPage']

    @property
    def blogs(self):
        # Get list of live blog pages that are descendants of this page ordered by most recent
        return BlogPage.objects.live().descendant_of(self).order_by('-date')

    def get_context(self, request):
        # Get blogs
        blogs = self.blogs

        # Filter by tag
        tag = request.GET.get('tag')
        if tag:
            blogs = blogs.filter(tags__name=tag)

        # Filter by date
        filter_date = request.GET.get('date')
        if filter_date:
            filter_date = datetime.strptime(filter_date, '%Y-%m')
            blogs = blogs.filter(date__month=filter_date.month, date__year=filter_date.year)

        # Pagination
        paginator = EllipsisPaginator(blogs, 10)  # Show 10 blogs per page
        try:
            blogs = paginator.page(request.GET.get('page'))
        except PageNotAnInteger:
            blogs = paginator.page(1)
        except EmptyPage:
            blogs = paginator.page(paginator.num_pages)

        # Update template context
        context = super(BlogIndexPage, self).get_context(request)
        context['blogs'] = blogs
        context['paginator'] = paginator
        return context


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey('blog.BlogPage', related_name='tagged_items')


class BlogPage(Page):
    # Parent page/subpage rules
    parent_page_types = ['blog.BlogIndexPage']

    body = StreamField(BlogStreamBlock())
    intro = RichTextField(help_text="This is displayed on the home and blog listing pages")
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    date = models.DateTimeField("Post date", default=timezone.now)

    @property
    def blog_index(self):
        # Find closest ancestor which is a blog index
        return self.get_ancestors().type(BlogIndexPage).last()

    def get_context(self, request):
        context = super(BlogPage, self).get_context(request)
        context['body'] = self.body
        return context


BlogPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('intro'),
    FieldPanel('date'),
    StreamFieldPanel('body'),
]

BlogPage.promote_panels = Page.promote_panels + [
    FieldPanel('tags'),
]


class AboutPage(Page):
    # Parent page/subpage rules
    parent_page_types = ['blog.HomePage', 'blog.AboutPage']
    subpage_types = ['blog.AboutPage']

    body = StreamField(BlogStreamBlock())
    full_title = models.CharField(max_length=255, blank=True, null=True)

    @property
    def children(self):
        return AboutPage.objects.live().descendant_of(self).order_by('title')

    @property
    def is_child(self):
        return type(self.get_parent().specific) is not HomePage

    def get_context(self, request):
        context = super(AboutPage, self).get_context(request)
        context['body'] = self.body
        context['children'] = self.children
        return context


AboutPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('full_title'),
    StreamFieldPanel('body'),
]
