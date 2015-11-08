from django.conf.urls import patterns, url

urlpatterns = patterns('deal.views',
    url(r'^$', 'index'),
    url(r'^get_item/$', 'get_item'),
    url(r'^buy_stock/$', 'buy_stock'),
    url(r'^sell_stock/$', 'sell_stock'),
)