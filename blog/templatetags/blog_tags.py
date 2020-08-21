from datetime import datetime
from django import template

import sys

from django.utils import timezone
from django.utils.safestring import mark_safe
from wagtail.core.rich_text import expand_db_html

from events.models import EventPage, EventsIndexPage

from blog.models import BlogPage, BlogIndexPage, CodeBlock, SocialMedia

from collections import OrderedDict

register = template.Library()


@register.inclusion_tag(
    'blog/tags/blog_sidebar.html',
    takes_context=True
)
def blog_sidebar(context, show_archives=None, show_tags=False, show_children=False, parent=None, archive_year=None,
                 archive_count=sys.maxsize):
    blog_index = BlogIndexPage.objects.live().in_menu().first()

    if show_archives:
        archives = OrderedDict()
        for blog in BlogPage.objects.live().order_by('-date'):
            archives.setdefault(blog.date.year, {}).setdefault(blog.date.month, []).append(
                blog)
    else:
        archives = None

    if show_children and parent:
        children = parent.children
    else:
        children = None

    return {
        'blog_index': blog_index,
        'archives': archives,
        'archive_year': archive_year or timezone.now().year,
        'children': children,
        'show_tags': show_tags,
        'archive_count': archive_count,
        'filter_date': context.get('filter_date'),
        'filter_tag': context.get('filter_tag'),
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


# Blog feed for home page
@register.inclusion_tag(
    'blog/tags/blog_listing_homepage.html',
    takes_context=True
)
def blog_listing_homepage(context, count=5):
    blogs = BlogPage.objects.live().order_by('-date')
    blog_index = BlogIndexPage.objects.live().in_menu().first()

    archives = dict()
    for blog in blogs:
        archives.setdefault(blog.date.year, {}).setdefault(blog.date.month, []).append(blog)

    return {
        'blogs': blogs[:count],
        'blog_index': blog_index,
        'archives': archives,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


# Event feed for home page
@register.inclusion_tag(
    'blog/tags/event_listing_homepage.html',
    takes_context=True
)
def event_listing_homepage(context, count=3):
    events = EventPage.objects.live().filter(finish__gte=timezone.now()).order_by('start')[:count]

    return {
        'events': events,
        'event_list': EventsIndexPage.objects.live().first(),
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


@register.inclusion_tag(
    'blog/tags/search_filters.html',
    takes_context=True
)
def search_filters(context):
    archive_date = context['request'].GET.get('date')

    if archive_date:
        archive_date = datetime.strftime(datetime.strptime(archive_date, '%Y-%m'), '%B %Y')

    return {
        'archive_date': archive_date,
        'tag': context['request'].GET.get('tag'),
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


@register.inclusion_tag(
    'blog/tags/social_bubbles.html',
    takes_context=True
)
def social_bubbles(context):
    return {
        'socials': SocialMedia.objects.all(),
        'request': context['request'],
    }


@register.filter
def get_code_language(language):
    return dict(CodeBlock.LANGUAGE_CHOICES)[language]


@register.filter
def to_month_str(value):
    return {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December',
    }[value]


@register.filter
def inlinerichtext(value):
    if value is None:
        html = ''
    else:
        if isinstance(value, str):
            html = expand_db_html(value)
        else:
            raise TypeError(
                "'richtext' template filter received an invalid value; expected string, got {}.".format(type(value)))
    html = html.replace('<p>', '')
    html = html.replace('</p>', '')
    return mark_safe(html)
