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
def stock_request(request):
    data = list()
    try:
        if request.POST.get("which", "") == "masu":
            count = int(request.POST.get("how_many", ""))
            stock = Stock.objects.get(StockItem=request.POST.get("item", ""))
            user = UserProfile.objects.get(username=request.user.username)
            stock_check = HaveStock.objects.get(owner=user, stockitem=stock)

            if stock.StockPrice * count > user.usermoney:
                raise print("돈이 부족합니다 ㅠㅠ")

            if stock_check.DoesNotExist is not True:
                count += stock_check.count
                HaveStock.objects.filter(owner=user, stockitem=stock).update(count=count)
                user.usermoney -= count * stock.StockPrice
                user.save()

            else:
                HaveStock.objects.create(owner=request.user, stockitem=stock,
                                         count=count, old_stockprice=stock.StockPrice)
                user.usermoney -= stock.StockPrice * count
                user.save()
        elif request.POST.get("which", "") == "mado":
            print(request.POST.get("item", ""))

        else:
            print("Fuck")
    except:
        print('error')
    return redirect('/after_deal/')
