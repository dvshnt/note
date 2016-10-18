from server import views

from server.settings.sites import bmshow as settings

from django.views import static
from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()


urlpatterns = [

    ## Standard Django admin endpoints for a crude CMS
    url(r'^admin/', include(admin.site.urls)),

    ## static page endpoints
    url(r'^$', views.index, name='index'),

    # ## user actions
    url(r'^issue/(?P<id>\d+)$', views.issue_view, name='view issue'),
    
    url(r'^v1/subscribe$', views.list_subscribe, name='list subscribe'),
    url(r'^v1/unsubscribe/(?P<hash>\w+)$', views.list_unsubscribe, name='list unsubscribe'),
    url(r'^v1/(?P<hash>\w+)/(?P<track_id>\w+)$', views.track_open, name='track open'),
    
    url(r'^tinymce/', include('tinymce.urls')),

    url(r'^media/(?P<path>.*)$', static.serve,
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True }
    ),

] +  staticfiles_urlpatterns()