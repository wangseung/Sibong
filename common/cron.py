import random
from datetime import datetime

from common.models import Stock, StockPrice, News, Newslist, Sospi, HaveStock, UserProfile, Compare


def add_news():
    news = News.objects.all()
    stocks = Stock.objects.all()
    stockp = StockPrice.objects.all()
    user = UserProfile.objects.all()
    sospi = Sospi.objects
    today = datetime.now()
    var_list = []

    for i in range(0, 5):
        rand_news = random.choice(news)
        content = stocks[i].StockItem + " " + rand_news.content
        price = stockp.filter(StockItem_id=stocks[i].id).order_by('-id')[0].StockPrice
        var_list.append(rand_news.variation)
        price += int(price * rand_news.variation / 100)
        if price < 0:
            price=1000
        createprice = StockPrice.objects.create(StockPrice=price, StockItem_id=stocks[i].id, fluctuation=rand_news.variation)
        createprice.save()

        createnews = Newslist.objects.create(content=content, stock=stocks[i].StockItem)
        createnews.save()

        average = sum(var_list) / len(stocks)
        nowsospi = sospi.all().order_by('-id')[0].data
        s = Sospi.objects.create(data=(average * 10 + nowsospi), day=int(today.day), month=int(today.month), fluctuation=average)
        s.save()

    for i in user:
        have_stock = HaveStock.objects.filter(owner=i)
        my_money = i.usermoney
        money = 0
        com = 0
        for j in have_stock:
            id = StockPrice.objects.all().filter(id=j.my_stock_id)[0].StockItem_id
            nowprice = StockPrice.objects.all().filter(StockItem_id=id).order_by('-id')[1].StockPrice
            price = j.buy_price - nowprice
            com += price * j.count
        if len(have_stock) != 0:
            Compare.objects.create(owner_id=i.id, compare=com)
            c = Compare.objects.filter(owner_id=i.id).order_by('-id')
            money = c[1].compare - c[0].compare
            my_money += money
            UserProfile.objects.filter(id=i.id).update(usermoney=my_money)

def compare():
    user = UserProfile.objects.all()
    for i in user:
        havestock = HaveStock.objects.filter(owner=i.id)
        money = i.usermoney
        for j in havestock:
            id = StockPrice.objects.all().filter(id=j.my_stock_id)[0].StockItem_id
            nowprice = StockPrice.objects.all().filter(StockItem_id=id).order_by('-id')[0].StockPrice
            money += nowprice * j.count
        UserProfile.objects.filter(id=i.id).update(old_usermoney=money)



