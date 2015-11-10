"""sibong URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'common.views.login'),
    url(r'^after_login/$', 'common.views.after_login'),
    url(r'^logout/$', 'common.views.logout'),
    url(r'^get_graph_data/$', 'common.views.get_graph_data'),
    url(r'^get_items/$', 'common.views.get_items'),
    url(r'^main/$', 'common.views.main'),
    url(r'^get_rank/$', 'common.views.get_rank'),
    url(r'^get_news/$', 'common.views.get_news'),
    url(r'^news/$', 'common.views.news'),
    url(r'^sospi/$', 'common.views.sospi'),
    url(r'^stock_item/$', 'common.views.stock_item'),
    url(r'^get_daily_data/$', 'common.views.get_daily_data'),
    url(r'^$', 'common.views.login'),
    url(r'^after_deal/$', 'common.views.after_deal'),
    url(r'^deal/', include('deal.urls')),
    url(r'^mypage/', include('mypage.urls')),
    url(r'^get_more_news', 'common.views.get_more_news')
]
