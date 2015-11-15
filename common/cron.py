import random
from datetime import datetime

from common.models import Stock, StockPrice, News, Newslist, Sospi, HaveStock, UserProfile


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
            money = i.usermoney
            for j in have_stock:
                id = StockPrice.objects.all().filter(id=j.my_stock_id)[0].StockItem_id
                nowprice = StockPrice.objects.all().filter(StockItem_id=id).order_by('-id')[0].StockPrice
                money += nowprice * j.count
            UserProfile.objects.filter(id=i.id).update(usermoney=money)

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



