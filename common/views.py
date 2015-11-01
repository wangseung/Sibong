from django.db import IntegrityError
from django.shortcuts import render, HttpResponse, redirect, render_to_response
from django.contrib import auth
from django.contrib.auth import login as auth_login, logout as auth_logout
# Create your views here.

from common.models import UserProfile, HaveStock, News, Stock
import simplejson as json

def login(request):

    results = {}
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if UserProfile.objects.filter(username=username).exists() is not True:
            user_create = UserProfile.objects.create(username=username,usermoney=10000000,havestock='')
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


def get_items(request):
    return HttpResponse('[{"item":"Layer7"},{"item":"BFD"},{"item":"Focus"},{"item":"Nefuse"},{"item":"Unifox"}]',content_type='application/json')
def get_graph_data(request):
    return HttpResponse('[20,19,20,21,24,23,20,17,14,13,9,12,15,19,20,25,28,30]',content_type='application/json')
def get_news(request):
    return HttpResponse('[{"content":"속보입니다.속보 속보요 속보"},{"content":"속보입니다.속보 속보요 속보"},{"content":"속보입니다.속보 속보요 속보"},{"content":"속보입니다.속보 속보요 속보"},{"content":"속보입니다.속보 속보요 속보"}]', content_type='application/json')
def get_rank(request):
    return HttpResponse('[{"item":"layer7"},{"item":"nefus"},{"item":"uni"},{"item":"team"},{"item":"focus"},{"item":"asd"},{"item":"NEFUS"},{"item":"NEFUS"},{"item":"NEFUS"},{"item":"NEFUS"}]', content_type='application/json')
def get_daily_data(request):
    return HttpResponse('[{"date":"10\/13","price":"35,000","percent":"3","plus_minus":"1"},{"date":"10\/12","price":"35,000","percent":"33","plus_minus":"-1"},{"date":"10\/11","price":"40,000","percent":"3","plus_minus":"1"},{"date":"10\/10","price":"35,000","percent":"3","plus_minus":"1"},{"date":"10\/9","price":"14,000","percent":"0","plus_minus":"0"},{"date":"10\/8","price":"35,000","percent":"2","plus_minus":"1"},{"date":"10\/7","price":"25,000","percent":"3","plus_minus":"-1"},{"date":"10\/6","price":"35,000","percent":"3","plus_minus":"1"},{"date":"10\/5","price":"2,000","percent":"0","plus_minus":"0"}]', content_type='application/json')

def buystock(request):
    count = 5
    stockname = 'layer7'
    stock = HaveStock.objects.create(owner=UserProfile.objects.get(id=1), mystock='', count=count)
    return True

def sellstock(requeset):
    return True

def main(request):
    return render(request, 'main.html')