from django.conf.urls import patterns, include, url


urlpatterns = patterns('get.views',
    url(r'^$',                       'index', name='get_index'),
)

