from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$','main.views.begin'),
    url(r'^users/$','main.views.users'),
    url(r'^about/$','main.views.about'),
    url(r'^recipes/$','main.views.recipes_list'),
    url(r'^recipe/(?P<id_recipe>\d+)$','main.views.detail_recipe'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
		{'document_root':settings.MEDIA_ROOT,}
	),
    url(r'^contact/$','main.views.contact'),
    url(r'^recipe/new/$','main.views.new_recipe'),
    url(r'^comments/$','main.views.new_comment'),
    url(r'^user/new$','main.views.new_user'),
    url(r'^enter/$','main.views.enter'),
    url(r'^private/$','main.views.private'),
    url(r'^close/$', 'main.views.close'),
)
