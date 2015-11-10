from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, Http404

from common.models import Stock, UserProfile, HaveStock
# Create your views here.

def index(request):
    return render(request, 'deal.html')

@csrf_exempt
def get_items(request):
    stock_list=[]
    stocks = Stock.objects.all()
    for i in stocks:
        stock_list.append(dict(item=str(i.StockItem)))
    send_stock_list = str(stock_list).replace(chr(39),chr(34))
    return HttpResponse(send_stock_list ,content_type='application/json')

@csrf_exempt
def stock_request(request):
    data = list()
    try:
        if request.POST.get("which", "") == "masu":
            count = int(request.POST.get("how_many", ""))
            stock = Stock.objects.get(StockItem=request.POST.get("item", ""))
            user = UserProfile.objects.get(username=request.user.username)
            stock_check = HaveStock.objects.filter(owner=user, mystock=stock)

            if (stock.StockPrice * count) > user.usermoney:
                raise Http404
            if stock_check.count() > 0:
                count += stock_check[0].count
                have = HaveStock.objects.get(owner=user, mystock=stock)
                have.count = count
                user.usermoney -= stock_check[0].count * stock.StockPrice
                user.save()
                have.save()
            else:
                HaveStock.objects.create(owner=request.user, mystock=stock,
                                         count=count, buy_price=stock.StockPrice)
                user.usermoney -= stock.StockPrice * count
                user.save()
        elif request.POST.get("which", "") == "mado":
            

        else:
            print("Fuck")

    except:
        print('error')
    return redirect('/after_deal/')
