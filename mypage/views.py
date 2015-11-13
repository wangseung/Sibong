from django.shortcuts import render, HttpResponse, redirect, render_to_response
from django.views.decorators.csrf import csrf_exempt
from common.models import UserProfile, HaveStock, News, Stock

import operator
# Create your views here.
@csrf_exempt
def get_rank(request):
    users = UserProfile.objects.all().order_by('-usermoney')
    users_money = list()
    moneys = list()
    """
    for i in users:
        have_stock = HaveStock.objects.filter(owner=i)
        money = i.usermoney
        for j in have_stock:
            money += j.mystock.StockPrice * j.count
        moneys.append(money)
    moneys.sort(reverse=True)
    print(moneys)
    """
    sorted_dic = list()
    dic = {}
    for i in users:
        have_stock = HaveStock.objects.filter(owner=i)
        money = i.usermoney
        for j in have_stock:
            money += j.mystock.StockPrice * j.count
        dic[i.username]=money

        #users_money.append(dict(name=str(i.username), asset=money))
    sorted_dic = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)
    print(sorted_dic)
    for i in sorted_dic:
        users_money.append(dict(name=str(i[0]), asset=int(i[1])))
    send_userlist = str(users_money).replace(chr(39),chr(34))
    return HttpResponse(send_userlist , content_type='application/json')


@csrf_exempt
def get_account(request):
    user = UserProfile.objects.get(username=request.user.username)
    have_stock = HaveStock.objects.filter(owner=user)
    sendlist = list()
    for i in have_stock:
        if i.count <= 0:
            pass
        else:
            sendlist.append(dict(item=str(i.mystock.StockItem), past=i.buy_price,
                                profit=int(i.mystock.StockPrice - i.buy_price),
                                now=i.mystock.StockPrice, have=i.count))
    send_list = str(sendlist).replace(chr(39),chr(34))
    return HttpResponse(send_list , content_type='application/json')

@csrf_exempt
def get_earn(request):
    send_value = list()
    value = list()
    user = UserProfile.objects.get(username=request.user.username)
    have_stock = HaveStock.objects.filter(owner=user)
    money = user.usermoney
    for i in have_stock:
        money += i.mystock.StockPrice * i.count

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
    user = UserProfile.objects.get(username=request.user.username)
    have_stock = HaveStock.objects.filter(owner=user)
    money = user.usermoney
    for i in have_stock:
        money += i.mystock.StockPrice * i.count
    send_value.append(dict(value=money))
    send_value = str(send_value).replace(chr(39),chr(34))
    return HttpResponse(send_value, content_type='application/json')

def index(request):
    return render(request, 'mypage.html')