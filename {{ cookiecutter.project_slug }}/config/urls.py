"""
{{ cookiecutter.project_name }} URL Configuration
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("{{ cookiecutter.project_slug }}.pages.urls")),
    path("users/", include("{{ cookiecutter.project_slug }}.users.urls")),
]
