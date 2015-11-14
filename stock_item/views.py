from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, Http404

from common.models import *

stock = ""

@csrf_exempt
def stock_item(request):
    stock = request.path
    return render(request,'stock_item.html')


@csrf_exempt
def get_graph_data(request):
    stockname = request.path_info.split('/')[3]
    data = []
    id = Stock.objects.all().filter(StockItem=str(stockname))
    print(id[0].id)
    s = StockPrice.objects.all().filter(StockItem=int(id[0].id)).order_by('-id')
    print(len(s))
    if request.POST.get('data') == 'day':
        print("asd")
        for i in s[:48]:
            print(i)
            data.append(i.StockPrice)
    elif request.POST.get('data') == 'week':
        for i in s[:336]:
            data.append(i.StockPrice)
    data.reverse()
    print(data)
    return HttpResponse(str(data), content_type='application/json')