from django.shortcuts import render, HttpResponse, redirect, render_to_response
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from common.models import UserProfile, HaveStock, News, Stock
# Create your views here.
@csrf_exempt
def get_rank(request):
    users = UserProfile.objects.all().order_by('-usermoney')
    users_money = list()
    for i in users:
        have_stock = HaveStock.objects.filter(owner=i)
        money = i.usermoney
        for j in have_stock:
            money += j.stockitem.StockPrice * j.count
        users_money.append(dict(name=str(i.username), asset=money))
    send_userlist = str(users_money).replace(chr(39),chr(34))
    return HttpResponse(send_userlist , content_type='application/json')


@csrf_exempt
def get_account(request):
    user = UserProfile.objects.filter(username=request.user)[0]
    have = HaveStock.objects.filter(owner=user)[0]
    sendlist = list()
    sendlist.append(dict(item=str(have.stockitem.StockItem), past=int(1000000), profit=int(),
                         now=have.stockitem.StockPrice, have=have.count))
    send_list = str(sendlist).replace(chr(39),chr(34))
    return HttpResponse(send_list , content_type='application/json')

@csrf_exempt
def get_earn(request):
    send_value = list()
    value = list()
    user = UserProfile.objects.filter(username=request.user)[0]
    have_stock = HaveStock.objects.filter(owner=user)
    money = user.usermoney
    for i in have_stock:
        money += i.stockitem.StockPrice * i.count

    earn = (money - user.old_usermoney) / user.old_usermoney * 100
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
    user = UserProfile.objects.filter(username=request.user)[0]
    have_stock = HaveStock.objects.filter(owner=user)
    money = user.usermoney
    for i in have_stock:
        money += i.stockitem.StockPrice * i.count
    send_value.append(dict(value=money))
    send_value = str(send_value).replace(chr(39),chr(34))
    return HttpResponse(send_value, content_type='application/json')

def index(request):
    return render(request, 'mypage.html')