"""
{{ cookiecutter.project_name }} URL Configuration
"""

from django.contrib import admin
from django.urls import path, include
from django.views import defaults as default_views
from django.conf.urls.static import static
from django.conf import settings

{%- if cookiecutter.use_wagtail == "y" %}

urlpatterns = [
    path('django-admin/', admin.site.urls),
    path('admin/', include("wagtail.admin.urls")),
    path("", include("{{ cookiecutter.project_slug }}.pages.urls")),
    path("users/", include("{{ cookiecutter.project_slug }}.users.urls")),
    path('documents/', include("wagtail.documents.urls")),
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's serving mechanism
    path("", include("wagtail.urls")),
]{%- else %}

urlpatterns = [
    path('admin/', include(admin.urls)),
    path("", include("{{ cookiecutter.project_slug }}.pages.urls")),
    path("users/", include("{{ cookiecutter.project_slug }}.users.urls")),
]{% endif %}

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += (
        staticfiles_urlpatterns()
    )  # tell gunicorn where static files are in dev mode
    urlpatterns += static(
        settings.MEDIA_URL + "images/",
        document_root=str(settings.MEDIA_ROOT / "images"),
    )
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=str(settings.MEDIA_ROOT),
    )

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
