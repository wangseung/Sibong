from django.conf.urls import patterns, url

urlpatterns = patterns('mypage.views',
    url(r'^$', 'index'),
    url(r'^get_rank/$', 'get_rank'),
    url(r'^get_value/$', 'get_value'),
)