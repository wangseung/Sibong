from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin


class UserProfile(AbstractUser):
    usermoney = models.IntegerField(null=True)
    old_usermoney = models.IntegerField(default=10000000)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

class Stock(models.Model):
    StockItem = models.CharField(max_length=30,unique=True)

class StockPrice(models.Model):
    StockItem = models.ForeignKey('Stock')
    StockPrice = models.IntegerField()
    fluctuation = models.IntegerField(default=0)

class HaveStock(models.Model):
    owner = models.ForeignKey(UserProfile)
    my_stock = models.ForeignKey('StockPrice')
    buy_price = models.IntegerField(null=True)
    count = models.IntegerField()

class News(models.Model):
    content = models.CharField(max_length=2048)
    variation = models.IntegerField()

class Newslist(models.Model):
    stock = models.CharField(max_length=20, default="")
    content = models.CharField(max_length=2048)

class Sospi(models.Model):
    data = models.IntegerField()
    day = models.IntegerField(default=0)
    month = models.IntegerField(default=0)
    fluctuation = models.IntegerField(default=0)