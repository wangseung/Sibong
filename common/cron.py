import random
from datetime import date

from common.models import Stock, StockPrice, News, Newslist, Sospi


def add_news():
    news = News.objects.all()
    stocks = Stock.objects.all()
    stockp = StockPrice.objects.all()
    sospi = Sospi.objects
    today = date.today()
    var_list = []

    for i in range(0, 5):
        rand_news = random.choice(news)
        content = stocks[i].StockItem + " " + rand_news.content
        price = stockp.filter(StockItem_id=stocks[i].id).order_by('-id')[0].StockPrice
        var_list.append(rand_news.variation)
        if price > 10000:
            price = int(price + rand_news.variation * 1000)
        createprice = StockPrice.objects.create(StockPrice=price, StockItem_id=stocks[i].id)
        createprice.save()

        createnews = Newslist.objects.create(content=content)
        createnews.save()

    average = sum(var_list) / len(stocks)
    nowsospi = sospi.all().order_by('-id')[0].data
    sospi.create(data=(average * 10 + nowsospi), day=int(today.day), month=int(today.month), fluctuation=average)
    sospi.save()
