from django.conf.urls import patterns, include, url
from evospacevariant import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'evospacevariant.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^$', 'shapes.views.home', name='home'),
    url(r'espanol/$', 'shapes.views.inicio', name='inicio'),
    url(r'^facebook/get_login/?$', 'shapes.views.facebook_get_login', name='facebook_get_login'),
    url(r'^facebook/login/?$', 'shapes.views.facebook_login', name='facebook_login'),
    url(r'^logout/?$', 'shapes.views.logout_view', name='logout_view'),
    url(r'^individual/(\d+)/$', 'shapes.views.individual_view', name='individual_view'),
    url(r'^EvoSpace/?$', 'shapes.views.evospace', name='evospace'),
    url(r'^add_collection/(\d+)/$', 'shapes.views.add_collection', name='add_collection'),
    url(r'^get_user_collections/(\d+)/$', 'shapes.views.get_user_collections', name='get_user_collections'),
    url(r'^add_ind_to_col/(\d+)/$', 'shapes.views.add_ind_to_col', name='add_ind_to_col'),
    url(r'^get_collection/(\d+)/$', 'shapes.views.get_collection', name='get_collection'),
    url(r'^get_collection/(\d+)/(\d+)$', 'shapes.views.get_collection', name='get_collection'),
    url(r'^dashboard/$', 'shapes.views.dashboard', name='dashboard'),
    url(r'^home2/$', 'shapes.views.home2', name='home2'),
    url(r'^get_user_level/(\d+)/$', 'shapes.views.get_user_level', name='get_user_level'),
    url(r'^get_user_level/(\w+)/$', 'shapes.views.get_user_level', name='get_user_level'),
    

    url(r'^admin/', include(admin.site.urls)),
)
