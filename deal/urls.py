from django.conf.urls import patterns, url

urlpatterns = patterns('deal.views',
    url(r'^$', 'index'),
    url(r'^get_items/$', 'get_items'),
    url(r'^stock_request/$', 'stock_request'),
)