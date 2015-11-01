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
def get_items(request):
    return HttpResponse('[{"item":"Focus"},{"item":"BFD"},{"item":"Layer7"},{"item":"Nefuse"},{"item":"Unifox"}]',content_type='application/json')
def get_graph_data(request):
    return HttpResponse('[20,19,20,21,24,23,20,17,14,13,9,12,15,19,20,25,28,30]',content_type='application/json')
def get_news(request):
    return HttpResponse('[{"content":"속보입니다.속보 속보요 속보"},{"content":"속보입니다.속보 속보요 속보"},{"content":"속보입니다.속보 속보요 속보"},{"content":"속보입니다.속보 속보요 속보"},{"content":"속보입니다.속보 속보요 속보"}]', content_type='application/json')
def get_rank(request):
    return HttpResponse('[{"item":"NEFUS"},{"item":"layer"},{"item":"uni"},{"item":"team"},{"item":"focus"},{"item":"asd"},{"item":"NEFUS"},{"item":"NEFUS"},{"item":"NEFUS"},{"item":"NEFUS"}]', content_type='application/json')

def buystock(request):
    count = 5

    stock = HaveStock.objects.create(owner=UserProfile.objects.get(id=1), mystock='', count=count)
    return True

def sellstock(requeset):
    return True

def main(request):
    return render(request, 'main.html')