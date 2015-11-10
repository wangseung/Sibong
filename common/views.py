import random
import time

from django.db import IntegrityError
from django.shortcuts import render, HttpResponse, redirect, render_to_response
from django.contrib import auth
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

from common.models import UserProfile, HaveStock, News, Stock, Newslist, Sospi

def login(request):
    results = {}
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if UserProfile.objects.filter(username=username).exists() is not True:
            user_create = UserProfile.objects.create(username=username,usermoney=10000000)
            user_create.set_password(password)
            user_create.save()
            results['error'] = "Success Register.\nPlease login"
            return render(request, 'index.html', results)
        if user is not None:
            auth_login(request,user)
            return redirect('/after_login/')
        else:
            results['error'] = "Wrong!, Try Again!"
    return render(request, 'index.html',results)

def after_login(request):
    return render(request, 'after_login.html')

def logout(request):
    auth_logout(request)
    return redirect('/login/')

def sospi(request):
    return render(request, 'sospi.html')

def news(request):
    return render(request, 'news.html')

def stock_item(request):
    return render(request, 'stock_item.html')

@csrf_exempt
def get_items(request):
    stock_list=[]
    stocks = Stock.objects.all()
    for i in range(len(stocks)):
        stock_list.append(dict(item=str(stocks[i].StockItem)))
    send_stock_list = str(stock_list).replace(chr(39),chr(34))
    return HttpResponse(send_stock_list ,content_type='application/json')


@csrf_exempt
def get_graph_data(request):
    data = []
    s = Sospi.objects.all().order_by('-id')
    if request.POST.get('data') == 'day':
        for i in s[:48]:
            data.append(i.data)
    elif request.POST.get('data') == 'week':
        for i in s[:336]:
            data.append(i.data)
    data.reverse()
    return HttpResponse(str(data), content_type='application/json')


@csrf_exempt
def get_news(request):
    newslist = Newslist.objects.all().order_by('-id')[:5]
    send_newslist = []
    for i in newslist:
        send_newslist.append(dict(content=str(i.content)))
    send_newslist = str(send_newslist).replace(chr(39),chr(34))
    return HttpResponse(send_newslist, content_type='application/json')

@csrf_exempt
def get_more_news(request):
    newslist = Newslist.objects.all().order_by('-id')
    send_newslist = []
    for i in newslist:
        send_newslist.append(dict(content=str(i.content)))
    send_newslist = str(send_newslist).replace(chr(39),chr(34))
    return HttpResponse(send_newslist, content_type='application/json')


@csrf_exempt
def get_rank(request):
    stocks = Stock.objects.all().order_by('-StockPrice')
    stocklist = []
    for i in stocks:
        stocklist.append(dict(item=str(i.StockItem)))
    send_stocklist = str(stocklist).replace(chr(39),chr(34))
    return HttpResponse(send_stocklist , content_type='application/json')

@csrf_exempt
def get_daily_data(request):
    return HttpResponse('[{"date":"10\/13","price":"35,000","percent":"3","plus_minus":"1"},{"date":"10\/12","price":"35,000","percent":"33","plus_minus":"-1"},{"date":"10\/11","price":"40,000","percent":"3","plus_minus":"1"},{"date":"10\/10","price":"35,000","percent":"3","plus_minus":"1"},{"date":"10\/9","price":"14,000","percent":"0","plus_minus":"0"},{"date":"10\/8","price":"35,000","percent":"2","plus_minus":"1"},{"date":"10\/7","price":"25,000","percent":"3","plus_minus":"-1"},{"date":"10\/6","price":"35,000","percent":"3","plus_minus":"1"},{"date":"10\/5","price":"2,000","percent":"0","plus_minus":"0"}]', content_type='application/json')


def buystock(request):
    count = 5
    stockname = 'layer7'
    stock = HaveStock.objects.create(owner=UserProfile.objects.get(id=1), mystock='', count=count)
    return True

def sellallstock(requeset):
    username = ""
    stockname = ""
    delstock = HaveStock.objects.filter(owner=username, mystock=stockname).delete()
    return True


def after_deal(request):
    return render(request, 'after_deal.html')

def main(request):
    data = request.POST.get('data', '')
    print(request.is_ajax())

    #if request.method == 'GET':
    print(data)
    return render(request, 'main.html')