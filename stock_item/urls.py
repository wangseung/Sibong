from django.conf.urls import patterns, url

urlpatterns = patterns('stock_item.views',
    url(r'^get_graph_data/', 'get_graph_data'),
    url(r'^get_price_data/', 'get_price_data'),
    url(r'^get_news/', 'get_news'),
    url(r'^', 'stock_item'),
)