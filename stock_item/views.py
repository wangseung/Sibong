from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, Http404

from common.models import *

stock = ""

@csrf_exempt
def stock_item(request):
    stock = request.path.split('/')[2]
    return render(request,'stock_item.html',context={'stock' : stock})


@csrf_exempt
def get_graph_data(request):
    stockname = request.path_info.split('/')[3]
    data = []
    id = Stock.objects.all().filter(StockItem=str(stockname))
    s = StockPrice.objects.all().filter(StockItem=int(id[0].id)).order_by('-id')
    if request.POST.get('data') == 'day':
        for i in s[:48]:
            data.append(i.StockPrice)
    elif request.POST.get('data') == 'week':
        for i in s[:336]:
            data.append(i.StockPrice)
    data.reverse()
    return HttpResponse(str(data), content_type='application/json')


@csrf_exempt
def get_price_data(request):
    stock = request.path.split('/')[3]
    stock_id = Stock.objects.all().filter(StockItem=str(stock))[0].id
    stockp = StockPrice.objects.all().filter(StockItem=int(stock_id)).order_by('-id')[0]

    price = stockp.StockPrice
    fluc = stockp.fluctuation
    feel = ""
    pm = 0
    if fluc > 0:
        pm = 1
        feel = "happy"
    elif fluc < 0:
        pm = -1
        fluc *= -1
        feel = "sad"
    senddict = dict(img=str(feel), value=str(price), percent=str(fluc), up_down=str(pm))
    senddict = str(senddict).replace(chr(39), chr(34))

    return HttpResponse(senddict,content_type='application/json')

@csrf_exempt
def get_news(request):
    stock = request.path.split('/')[3]
    newslist = Newslist.objects.all().filter(stock=stock).order_by('-id')[:6]
    send_newslist = []
    for i in newslist:
        send_newslist.append(dict(content=str(i.content), img=""))
    send_newslist = str(send_newslist).replace(chr(39), chr(34))
    return HttpResponse(send_newslist, content_type='application/json')
