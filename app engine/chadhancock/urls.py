"""Urls for twittertorss app."""

from django.conf.urls import defaults
from django.views import generic

# Url patterns
urlpatterns = defaults.patterns(
  '',
  defaults.url(
      r'^cams/$', generic.TemplateView.as_view(template_name='cams.html'),
      name='cams'),
  defaults.url(
      r'^$', generic.TemplateView.as_view(template_name='index.html'),
      name='index'),
)
