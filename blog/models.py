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
import bleach

from lib.ellipsis_paginator import EllipsisPaginator


@register_snippet
class FooterLink(models.Model):
    link_url = models.URLField(null=True, blank=True)
    title = models.CharField(max_length=20, blank=True)
    order = models.SmallIntegerField(default=0)

    panels = [
        FieldPanel('title'),
        FieldPanel('link_url'),
        FieldPanel('order')
    ]

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return self.title


@register_snippet
class SocialMedia(models.Model):
    url = models.URLField()
    icon = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    footer = models.BooleanField(default=True, help_text="Should this be shown in the footer")

    panels = [
        FieldPanel('name'),
        FieldPanel('url'),
        FieldPanel('icon'),
        FieldPanel('footer')
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
        return self.name + " (" + tier + ")"


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


domestos = bleach.Cleaner(
    tags=["a", "abbr", "address", "area", "article", "aside", "audio", "b", "bdi", "bdo", "blockquote", "body", "br",
          "button", "canvas", "caption", "cite", "code", "col", "colgroup", "data", "datalist", "dd", "del", "details",
          "dfn", "div", "dl", "dt", "em", "fieldset", "figcaption", "figure", "footer", "form", "h1", "h2", "h3", "h4",
          "h5", "h6", "header", "hr", "i", "iframe", "img", "input", "ins", "kbd", "label", "legend", "li", "map",
          "mark", "meter", "nav", "noscript", "ol", "optgroup", "option", "output", "p", "picture", "pre", "progress",
          "q", "rp", "rt", "ruby", "s", "samp", "section", "select", "small", "source", "span", "strong", "style",
          "svg", "sub", "summary", "sup", "table", "tbody", "td", "textarea", "tfoot", "th", "thead", "time", "tr",
          "track", "u", "ul", "var", "video", "wbr"],
    attributes={
        '*': ['style', 'dir', 'class', 'id', 'lang', 'tabindex', 'title', 'translate'],
        'a': ['download', 'href', 'hreflang', 'media', 'referrerpolicy', 'rel', 'target', 'type'],
        'area': ['alt', 'coords', 'download', 'href', 'hreflang', 'media', 'rel', 'shape', 'target', 'type'],
        'audio': ['autoplay', 'controls', 'loop', 'muted', 'preload', 'src'],
        'bdo': ['dir'],
        'blockquote': ['cite'],
        'button': ['autofocus', 'disabled', 'form', 'formaction', 'formenctype', 'formmethod', 'formnovalidate',
                   'formtarget', 'name', 'type', 'value'],
        'canvas': ['height', 'width'],
        'col': ['span'],
        'colgroup': ['span'],
        'data': ['value'],
        'del': ['cite', 'datetime'],
        'details': ['open'],
        'fieldset': ['disabled', 'form', 'name'],
        'form': ['accept-charset', 'action', 'autocomplete', 'enctype', 'method', 'name', 'novalidate', 'rel',
                 'target'],
        'iframe': ['allow', 'allowfullscreen', 'height', 'name', 'referrerpolicy', 'sandbox', 'src', 'srcdoc', 'width'],
        'img': ['alt', 'crossorigin', 'height', 'ismap', 'longdesc', 'referrerpolicy', 'sizes', 'src', 'srcset',
                'usemap', 'width'],
        'input': ['accept', 'alt', 'autocomplete', 'autofocus', 'checked', 'dirname', 'disabled', 'form', 'formaction',
                  'formenctype', 'formmethod', 'formnovalidate', 'formtarget', 'height', 'list', 'max', 'maxlength',
                  'min', 'minlength', 'multiple', 'name', 'pattern', 'placeholder', 'readonly', 'required', 'size',
                  'src', 'step', 'type', 'value', 'width'],
        'ins': ['cite', 'datetime'],
        'label': ['for', 'form'],
        'li': ['value'],
        'map': ['name'],
        'meter': ['form', 'high', 'low', 'max', 'min', 'optimum', 'value'],
        'ol': ['reversed', 'start', 'type'],
        'optgroup': ['disabled', 'label'],
        'option': ['disabled', 'label', 'selected', 'value'],
        'output': ['for', 'form', 'name'],
        'progress': ['max', 'value'],
        'q': ['cite'],
        'select': ['autofocus', 'disabled', 'form', 'multiple', 'name', 'required', 'size'],
        'source': ['media', 'sizes', 'src', 'srcset', 'type'],
        'style': ['media', 'type'],
        'td': ['colspan', 'headers', 'rowspan'],
        'textarea': ['autofocus', 'cols', 'dirname', 'disabled', 'form', 'maxlength', 'name', 'placeholder', 'readonly',
                     'required', 'rows', 'wrap'],
        'th': ['abbr', 'colspan', 'headers', 'rowspan', 'scope'],
        'time': ['datetime'],
        'track': ['default', 'kind', 'label', 'src', 'srclang'],
        'video': ['autoplay', 'controls', 'height', 'loop', 'muted', 'poster', 'preload', 'src', 'width']
    },
    styles=["align-content", "align-items", "align-self", "animation", "animation-delay", "animation-direction",
            "animation-duration", "animation-fill-mode", "animation-iteration-count", "animation-name",
            "animation-play-state", "animation-timing-function", "backface-visibility", "background",
            "background-attachment", "background-blend-mode", "background-clip", "background-color", "background-image",
            "background-origin", "background-position", "background-repeat", "background-size", "border",
            "border-bottom", "border-bottom-color", "border-bottom-left-radius", "border-bottom-right-radius",
            "border-bottom-style", "border-bottom-width", "border-collapse", "border-color", "border-image",
            "border-image-outset", "border-image-repeat", "border-image-slice", "border-image-source",
            "border-image-width", "border-left", "border-left-color", "border-left-style", "border-left-width",
            "border-radius", "border-right", "border-right-color", "border-right-style", "border-right-width",
            "border-spacing", "border-style", "border-top", "border-top-color", "border-top-left-radius",
            "border-top-right-radius", "border-top-style", "border-top-width", "border-width", "bottom",
            "box-decoration-break", "box-shadow", "box-sizing", "break-after", "break-before", "break-inside",
            "caption-side", "caret-color", "clear", "clip", "color", "column-count", "column-fill", "column-gap",
            "column-rule", "column-rule-color", "column-rule-style", "column-rule-width", "column-span", "column-width",
            "columns", "cursor", "direction", "display", "empty-cells", "filter", "flex", "flex-basis",
            "flex-direction", "flex-flow", "flex-grow", "flex-shrink", "flex-wrap", "float", "font", "font-family",
            "font-feature-settings", "font-kerning", "font-language-override", "font-size", "font-size-adjust",
            "font-stretch", "font-style", "font-synthesis", "font-variant", "font-variant-alternates",
            "font-variant-caps", "font-variant-east-asian", "font-variant-ligatures", "font-variant-numeric",
            "font-variant-position", "font-weight", "grid", "grid-area", "grid-auto-columns", "grid-auto-flow",
            "grid-auto-rows", "grid-column", "grid-column-end", "grid-column-gap", "grid-column-start", "grid-gap",
            "grid-row", "grid-row-end", "grid-row-gap", "grid-row-start", "grid-template", "grid-template-areas",
            "grid-template-columns", "grid-template-rows", "hanging-punctuation", "height", "hyphens",
            "image-rendering", "isolation", "justify-content", "@keyframes", "left", "letter-spacing", "line-break",
            "line-height", "list-style", "list-style-image", "list-style-position", "list-style-type", "margin",
            "margin-bottom", "margin-left", "margin-right", "margin-top", "max-height", "max-width", "@media",
            "min-height", "min-width", "mix-blend-mode", "object-fit", "object-position", "opacity", "order", "outline",
            "outline-color", "outline-offset", "outline-style", "outline-width", "overflow", "overflow-wrap",
            "overflow-x", "overflow-y", "padding", "padding-bottom", "padding-left", "padding-right", "padding-top",
            "perspective", "perspective-origin", "pointer-events", "position", "quotes", "resize", "right",
            "scroll-behavior", "tab-size", "table-layout", "text-align", "text-align-last", "text-combine-upright",
            "text-decoration", "text-decoration-color", "text-decoration-line", "text-decoration-style", "text-indent",
            "text-justify", "text-orientation", "text-overflow", "text-shadow", "text-transform",
            "text-underline-position", "top", "transform", "transform-origin", "transform-style", "transition",
            "transition-delay", "transition-duration", "transition-property", "transition-timing-function",
            "unicode-bidi", "user-select", "vertical-align", "visibility", "white-space", "width", "word-break",
            "word-spacing", "word-wrap", "writing-mode", "z-index"])


class HTMLBlock(StructBlock):
    value = TextBlock()

    class Meta:
        icon = 'cogs'

    def render(self, value, **kwargs):
        content = domestos.clean(str(value['value']))
        return mark_safe(content)


class BlogStreamBlock(StreamBlock):
    h2 = Heading2Block(icon="title", classname="title")
    h3 = Heading3Block(icon="title", classname="title")
    h4 = Heading4Block(icon="title", classname="title")
    paragraph = RichTextBlock(icon="pilcrow")
    image = ImageChooserBlock()
    pullquote = PullQuoteBlock()
    document = DocumentChooserBlock(icon="doc-full-inverse")
    code = CodeBlock()
    html = HTMLBlock()


class HomePage(Page):
    # Parent page/subpage rules
    subpage_types = ['blog.BlogIndexPage', 'blog.AboutPage', 'events.EventsIndexPage']

    description = StreamField(BlogStreamBlock())
    alert = RichTextField(blank=True, features=['bold', 'italic'])
    alert_link = models.URLField(blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('description'),
        MultiFieldPanel(
            [FieldPanel('alert'),
             FieldPanel('alert_link'),
             ], heading="Alert"),
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
