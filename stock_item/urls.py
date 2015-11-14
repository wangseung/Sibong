from django.conf.urls import patterns, url

urlpatterns = patterns('stock_item.views',
    url(r'^get_graph_data/', 'get_graph_data'),
    url(r'^', 'stock_item'),
)