from django.contrib import admin

from .models import UserProfile, HaveStock, Stock, Newslist, News

admin.site.register(UserProfile)
admin.site.register(HaveStock)
admin.site.register(Stock)
admin.site.register(Newslist)
admin.site.register(News)