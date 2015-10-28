from django.shortcuts import render, HttpResponse, redirect
from django.contrib import auth
from django.contrib.auth import login as auth_login, logout as auth_logout

from models import UserProfile

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


    return render(request, 'register.html', results)

def login(request):
    results = {}
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            print(user, user.is_active)
            auth_login(request,user)
        else:
            results['error'] = "Wrong!, Try Again!"

    return render(request, 'login.html', results)



def logout(request):
    auth_logout(request)
    return redirect('/login/')
