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