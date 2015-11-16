from django.shortcuts import render, HttpResponse, redirect, render_to_response
from django.views.decorators.csrf import csrf_exempt
from common.models import UserProfile, HaveStock, News, Stock, StockPrice

import operator
# Create your views here.
@csrf_exempt
def get_rank(request):
    users = UserProfile.objects.all().order_by('-usermoney')
    users_money = list()
    for i in users:
        users_money.append(dict(name=str(i.username), asset=int(i.usermoney)))
    send_userlist = str(users_money).replace(chr(39),chr(34))
    return HttpResponse(send_userlist , content_type='application/json')


@csrf_exempt
def get_account(request):
    user = UserProfile.objects.get(username=request.user.username)
    have_stock = HaveStock.objects.filter(owner=user)
    sendlist = list()
    for i in have_stock:
        stocklist = StockPrice.objects.filter(StockItem=i.my_stock.StockItem)
        now_price = stocklist[len(stocklist)-2].StockPrice
        if i.count <= 0:
            i.delete()
        else:
            sendlist.append(dict(item=str(i.my_stock.StockItem.StockItem), past=i.buy_price,
                                profit=int(now_price - i.buy_price),
                                now=now_price, have=i.count))
    send_list = str(sendlist).replace(chr(39),chr(34))
    return HttpResponse(send_list , content_type='application/json')

@csrf_exempt
def get_earn(request):
    value = list()
    user = UserProfile.objects.get(username=request.user.username)
    have_stock = HaveStock.objects.filter(owner=user)
    money = user.usermoney
    earn = (user.usermoney - user.old_usermoney) / user.old_usermoney * 100
    if earn < 0:
        earn *= -1
        plus_minus = -1
    elif earn == 0:
        plus_minus = 0
    else:
        plus_minus = 1
    value.append(dict(earn=earn, plus_minus=plus_minus))
    send_value = str(value).replace(chr(39),chr(34))
    return HttpResponse(send_value, content_type='application/json')

@csrf_exempt
def get_value(request):
    send_value = list()
    user = UserProfile.objects.get(username=request.user.username)
    have_stock = HaveStock.objects.filter(owner=user)
    money = user.usermoney
    send_value.append(dict(value=money))
    send_value = str(send_value).replace(chr(39),chr(34))
    return HttpResponse(send_value, content_type='application/json')

def index(request):
    return render(request, 'mypage.html')