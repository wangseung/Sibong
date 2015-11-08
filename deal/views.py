from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from common.models import Stock, UserProfile, HaveStock
# Create your views here.

def index(request):
    return render(request, 'deal.html')

@csrf_exempt
def get_item(request):
    stock_list=[]
    stocks = Stock.objects.all()
    for i in stocks:
        stock_list.append(dict(item=str(i.StockItem)))
    send_stock_list = str(stock_list).replace(chr(39),chr(34))
    return HttpResponse(send_stock_list ,content_type='application/json')

@csrf_exempt
def buy_stock(request):
    data = list()
    try:
        if request.POST.get('which', '') == "masu":
            count = int(request.POST.get('many', ''))
            print(count)
            stock = Stock.objects.filter(StockItem=request.POST.get('item', ''))[0]
            stock_check = HaveStock.objects.filter(owner=request.user)
            if stock_check.exists():
                already = HaveStock.objects.filter(owner=request.user, stockitem=stock)
                already.update(count=already.count+count)
            else:
                HaveStock.objects.create(owner=request.user, stockitem=stock, count=count)
                want_stock = Stock.objects.filter(StockItem='')[0]
                user = UserProfile.objects.filter(username=request.user.username)[0]
                user.usermoney -= want_stock.StockPrice * count
        else:
            print('error111')
    except:
        print('error')
    return redirect('/after_deal/')

def sell_stock(request):
    data = {}
    return redirect('/after_deal/')
