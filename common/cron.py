import random

from common.models import *

def add_news():
    stocks = list(Stock.objects.all())
    news = list(News.objects.all())
    for i in range(0, 5):
        rand_stock = random.choice(stocks)
        rand_news = random.choice(news)
        content = rand_stock.StockItem+" "+rand_news.content
        var_price = int(rand_stock.StockPrice + rand_news.variation * 100000)
        s = Stock.objects.filter(StockItem=str(rand_stock.StockItem))
        Stock.objects.filter(StockItem=s[0].StockItem).update(StockPrice=var_price)

        newscreate = Newslist.objects.create(content=content)
        newscreate.save()