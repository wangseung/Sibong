from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin


class UserProfile(AbstractUser):
    usermoney = models.IntegerField(null=True)
    old_usermoney = models.IntegerField(default=10000000)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

class HaveStock(models.Model):
    owner = models.ForeignKey(UserProfile)
    mystock = models.ForeignKey('StockPrice')
    buy_price = models.IntegerField(null=True)
    count = models.IntegerField()


class Stock(models.Model):
    StockItem = models.CharField(max_length=30,unique=True)

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

class StockPrice(models.Model):
    StockItem = models.ForeignKey(Stock)
    StockPrice = models.IntegerField()
    fluctuation = models.IntegerField(default=0)



#stock = HaveStock.objects.create(owner=UserProfile.objects.get(id=1),mystock='layer7',count=5)
#user = UserProfile.objects.create(username='admin',usermoney=999999999999)
#user.set_password('admina')
#user.save()