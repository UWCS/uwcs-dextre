import bleach
from django import template
from django.template.defaultfilters import safe
from django.utils.safestring import mark_safe

from blog.models import Sponsor, FooterLink, SocialMedia
from lib.html_cleaners import chlorox as chlorox_

from wagtail.core.models import Page, Site
from markdown import markdown

register = template.Library()


@register.filter()
def markdownify(value):
    return markdown(value)


@register.simple_tag(takes_context=True)
def url_replace(context, field, value):
    dict_ = context.request.GET.copy()

    dict_[field] = value

    return dict_.urlencode()


@register.filter()
def chlorox(field):
    return mark_safe(chlorox_.clean(field))


@register.simple_tag(takes_context=True)
def website_theme(context):
    return context["request"].session.get("website_theme", default="auto")


@register.inclusion_tag("lib/tags/sponsor_homepage.html", takes_context=True)
def sponsor_homepage(context):
    return {
        "sponsors": Sponsor.objects.filter(tier__gte=Sponsor.TIERS.SILVER).all(),
        "request": context["request"],
    }


@register.inclusion_tag("lib/tags/sponsor_sidebar.html", takes_context=True)
def sponsor_sidebar(context):
    return {
        "sponsors": Sponsor.objects.filter(tier__gte=Sponsor.TIERS.GOLD).all(),
        "request": context["request"],
    }


@register.simple_tag(takes_context=True)
def get_site_root(context):
    # NB this returns a core.Page, not the implementation-specific model used
    # so object-comparison to self will return false as objects would differ
    site = Site.find_for_request(context["request"])
    return site.root_page


# Retrieves the top menu items
@register.inclusion_tag("lib/tags/top_menu.html", takes_context=True)
def top_menu(context, parent, calling_page=None):
    menuitems = parent.get_children().live().in_menu()
    for menuitem in menuitems:
        # We don't directly check if calling_page is None since the template
        # engine can pass an empty string to calling_page
        # if the variable passed as calling_page does not exist.
        menuitem.active = (
            calling_page.startswith(menuitem.url) if calling_page else False
        )

    return {
        "calling_page": calling_page,
        "menuitems": menuitems,
        "is_home": calling_page == u"/",
        # required by the pageurl tag that we want to use within this template
        "request": context["request"],
    }


# Retrieves the footer items
@register.inclusion_tag("lib/tags/footer.html", takes_context=True)
def footer(context, parent):
    return {
        "parent": parent,
        "menuitems": FooterLink.objects.all(),
        "socials": SocialMedia.objects.filter(footer=True),
        # required by the pageurl tag that we want to use within this template
        "request": context["request"],
    }


@register.inclusion_tag("lib/tags/breadcrumbs.html", takes_context=True)
def breadcrumbs(context):
    self = context.get("self")
    if self is None or self.depth <= 2:
        # When on the home page, displaying breadcrumbs is irrelevant.
        ancestors = ()
    else:
        ancestors = Page.objects.ancestor_of(self, inclusive=True).filter(depth__gt=2)
    return {
        "ancestors": ancestors,
        "request": context["request"],
    }
