from django.db import IntegrityError
from django.shortcuts import render, HttpResponse, redirect, render_to_response
from django.contrib import auth
from django.contrib.auth import login as auth_login, logout as auth_logout
# Create your views here.

from common.models import UserProfile
print("aaac")

def register(request):
    results = {}
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        try:
            user = UserProfile.objects.create(username=username)
            user.set_password(password)
            user.save()
            return redirect('/login/')
        except :
            results['error'] = 'Already used!'

        #if UserProfile.objects.filter(username=username).exists():
        #    results['error'] = 'Already used!'
        #else:
        #    user = UserProfile.objects.create(username=username)
        #    user.set_password(password)
        #    user.save()
        #    return redirect('/login/')


    return render(request, '.html', results)

def login(request):
    results = {}
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if UserProfile.objects.filter(username=username).exists() is not True:
            user_create = UserProfile.objects.create(username=username)
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
    return HttpResponse('[{"item":"1111"},{"item":"2222"},{"item":"3333"},{"item":"4444"},{"item":"5555"},{"item":"6666"},{"item":"7777"},{"item":"8888"},{"item":"9999"},{"item":"101010"},{"item":"111111"}]',content_type='application/json')
def get_graph_data(request):
    return HttpResponse('[100,200,300,400,500,600,700,800,900,1000,100,200,300,400,500,600,700,800,900,1000,100,200,300,400,500,600,700,800,900,1000,100,200,300,400,500,600,700,800,900,1000,100,200,300,400,500,600,700,800,900,1000,100,200,300,400,500,600,700,800,900,1000,100,200,300,400,500,600,700,800,900,1000,100,200,300,400,500,600,700,800,900,1000,100,200,300,400,500,600,700,800,900,1000,100,200,300,400,500,600,700,800,900,1000,100,200,300,400,500,600,700,800,900,1000,100,200,300,400,500,600,700,800,900,1000,100,200,300,400,500,600,700,800,900,1000,100,200,300,400,500,600,700,800,900,1000,100,200,300,400,500,600,700,800,900,1000,100,200,300,400,500,600,700,800,900,1000,100,200,300,400,500,600,700,800,900,1000,100,200,300,400,500,600,700,800,900,1000,100,200,300,400,500,600,700,800,900,1000,100,200,300,400,500,600,700,800,900,1000,100,200,300,400,500,600,700,800,900,1000,100,200,300,400,500,600,700,800,900,1000,100,200,300,400,500,600,700,800,900,1000,100,200,300,400,500,600,700,800,900,1000,100,200,300,400,500,600,700,800,900,1000,100,200,300,400,500,600,700,800,900,1000,100,200,300,400,500,600,700,800,900,1000,100,200,300,400,500,600,700,800,900,1000,100,200,300,400,500,600,700,800,900,1000,100,200,300,400,500,600,700,800,900,1000,100,200,300,400,500,600,700,800,900,1000,100,200,300,400,500,600,700,800,900,1000,100,200,300,400,500,600,700,800,900,1000,100,200,300,400,500,600,700,800,900,1000,100,200,300,400,500,600,700,800,900,1000,100,200,300,400,500,600,700,800,900,1000,100,200,300,400,500,600,700,800,900,1000,100,200,300,400,500,600,700,800,900,1000,100,200,300,400,500,600,700,800,900,1000,100,200,300,400,500,600,700,800,900,1000,100,200,300,400,500,600,700,800,900,1000,100,200,300,400,500,600,700,800,900,1000,100,200,300,400,500,600,700,800,900,1000,100,200,300,400,500,600,700,800,900,1000,100,200,300,400,500,600,700,800,900,1000,100,200,300,400,500,600,700,800,900,1000,100,200,300,400,500,600,700,800,900,1000,100,200,300,400,500,600,700,800,900,1000,100,200,300,400,500,600,700,800,900,1000,100,200,300,400,500,600,700,800,900,1000,100,200,300,400,500,600,700,800,900,1000,100,200,300,400,500,600,700,800,900,1000]',content_type='application/json')



def main(request):
    return render(request, 'main.html')