from datetime import date

from django.shortcuts import render, HttpResponse, redirect, render_to_response
from django.contrib import auth
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.views.decorators.csrf import csrf_exempt

from common.models import UserProfile, HaveStock, News, Stock, Newslist, Sospi, StockPrice,Compare


def login(request):
    results = {}
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if UserProfile.objects.filter(username=username).exists() is not True:
            user_create = UserProfile.objects.create(username=username, usermoney=10000000)
            user_create.set_password(password)
            user_create.save()

            user_id = UserProfile.objects.filter(username=username)[0].id
            compare_create = Compare.objects.create(owner_id=user_id, compare=0)
            compare_create.save()

            results['error'] = "Success Register.\nPlease login"
            return render(request, 'index.html', results)
        if user is not None:
            auth_login(request, user)
            return redirect('/after_login/')
        else:
            results['error'] = "Wrong!, Try Again!"
    return render(request, 'index.html', results)


def after_login(request):
    return render(request, 'after_login.html')


@csrf_exempt
def logout(request):
    auth_logout(request)
    return redirect('/login/')


def sospi(request):
    return render(request, 'sospi.html')


def news(request):
    return render(request, 'news.html')


def after_deal(request):
    return render(request, 'after_deal.html')


def deal(request):
    return render(request, 'deal.html')


# @csrf_exempt
# def stock_item(request):
#    return render(request, 'stock_item.html')


def main(request):
    data = request.POST.get('data', '')
    # if request.method == 'GET':
    return render(request, 'main.html')


@csrf_exempt
def get_items(request):
    stock_list = []
    stocks = Stock.objects.all()
    for i in range(len(stocks)):
        stock_list.append(dict(item=str(stocks[i].StockItem)))
    send_stock_list = str(stock_list).replace(chr(39), chr(34))
    return HttpResponse(send_stock_list, content_type='application/json')


@csrf_exempt
def get_graph_data(request):
    data = []
    s = Sospi.objects.all().order_by('-id')
    if request.POST.get('data') == 'day':
        for i in s[1:49]:
            data.append(i.data)
    elif request.POST.get('data') == 'week':
        for i in s[1:337]:
            data.append(i.data)
    data.reverse()
    return HttpResponse(str(data), content_type='application/json')


@csrf_exempt
def get_news(request):
    newslist = Newslist.objects.all().order_by('-id')[:5]
    send_newslist = []
    for i in newslist:
        send_newslist.append(dict(content=str(i.content)))
    send_newslist = str(send_newslist).replace(chr(39), chr(34))
    return HttpResponse(send_newslist, content_type='application/json')


@csrf_exempt
def get_more_news(request):
    newslist = Newslist.objects.all().order_by('-id')
    send_newslist = []
    for i in newslist:
        send_newslist.append(dict(content=str(i.content)))
    send_newslist.append({"end": 'true'})
    send_newslist = str(send_newslist).replace(chr(39), chr(34))
    return HttpResponse(send_newslist, content_type='application/json')


@csrf_exempt
def get_rank(request):
    stocks = Stock.objects.all()
    stocklist = []
    stockdict = {}
    for i in stocks:
        stockp = StockPrice.objects.all().filter(StockItem_id=i.id).order_by('-id')[1].StockPrice
        stockdict.update({i.StockItem: stockp})
    for key in sorted(stockdict, key=stockdict.get, reverse=True):
        stocklist.append(dict(item=str(key)))
    send_stocklist = str(stocklist).replace(chr(39), chr(34))
    return HttpResponse(send_stocklist, content_type='application/json')


@csrf_exempt
def get_daily_data(request):
    sendlist = []
    t = date.today()
    for i in range(9):
        price = Sospi.objects.all().filter(day=(t.day - i)).order_by('-id')[0].data
        oldprice = Sospi.objects.all().filter(day=(t.day - (i+1))).order_by('-id')[0].data
        fluc = int(round((price/oldprice)*100 - 100))
        pm = 0
        if fluc > 0:
            pm = 1
        elif fluc < 0:
            pm = -1
            fluc *= -1

        sendlist.append(
            dict(date=str(t.month)+"/"+str(t.day - i), price=str(price), percent=str(fluc), plus_minus=str(pm)))

    sendlist = str(sendlist).replace(chr(39), chr(34))
    return HttpResponse(sendlist, content_type='application/json')



