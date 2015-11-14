import random

from common.models import Stock, StockPrice, News, Newslist


def add_news():
    news = News.objects.all()
    stocks = Stock.objects.all()
    stockp = StockPrice.objects.all()
    for i in range(0,5):
        rand_news = random.choice(news)
        content = stocks[i].StockItem + " " + rand_news.content
        price = stockp.filter(StockItem_id = stocks[i].id).order_by('-id')[0].StockPrice
        if price > 10000 :
            price = int(price + rand_news.variation * 100)
        createprice = StockPrice.objects.create(StockPrice=price, StockItem_id=stocks[i].id)
        createprice.save()
        print("asdf")
        createnews = Newslist.objects.create(content=content)
        createnews.save()
