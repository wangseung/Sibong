from django.shortcuts import render, HttpResponse, redirect, render_to_response
from django.views.decorators.csrf import csrf_exempt
from common.models import UserProfile, HaveStock, News, Stock
# Create your views here.

@csrf_exempt
def get_rank(request):
    users = UserProfile.objects.all().order_by('-usermoney')
    users_money = list()
    for i in users:
        users_money.append(int(i.usermoney))
    userlist = []
    for i in users:
        userlist.append(dict(name=str(i.username), asset=int(i.usermoney)))
    send_userlist = str(userlist).replace(chr(39),chr(34))
    return HttpResponse(send_userlist , content_type='application/json')



def index(request):
    return render(request, 'mypage.html')