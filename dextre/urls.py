from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

urlpatterns = [
    url(r"^admin/", admin.site.urls, name="django_admin"),
    url(r"^o/", include("oauth2_provider.urls", namespace="oauth2_provider")),
    url(r"^api/", include("api.urls")),
    url(r"^accounts/", include("accounts.urls")),
    url(r"^signups/", include("events.urls")),
    url(r"^report/", include("report.urls")),
    url(r"^cms/", include(wagtailadmin_urls)),
    url(r"^documents/", include(wagtaildocs_urls)),
    url(r"^markdownx/", include("markdownx.urls")),
    url(r"sso/", include("sp.urls")),
    url(r"", include(wagtail_urls)),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
