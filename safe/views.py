from django.shortcuts import render,redirect
from .models import Safe
from datetime import datetime
from user_auth.views import user_auth,register_page,login_page,logout_view

# Create your views here.
def index(request):
    context = {
        "register": register_page,
        "login": login_page
    }
    return render(request,"safe/index.html",context)

def userPage(request):
    username = request.session["username"]
    try:
        data = Safe.objects.filter(username=username).all()
    except Safe.DoesNotExist:
        data = None

    context = {
        "username": username,
        "datafields": data
    }
    return render(request,"safe/userPage.html",context)

def insert_page(request):
    if not request.user.is_authenticated:
        return redirect('login_page')
    # accessing session
    username = request.session['username']
    context = {
        "username": username,
        "logout": logout_view
    }
    return render(request,"safe/insert.html",context)

def insert(request):
    if request.method == 'POST':
        username = request.session["username"]
        website = request.POST.get('website')
        userInfo = request.POST.get('userInfo')
        password = request.POST.get('password')
        check = request.POST.get('check')
        dateTime = datetime.now()

        if check == "on": # checkbox state can be on | None
            new = Safe(username=username,website=website,userInfo=userInfo,password=password,dateTime=dateTime)
            new.save()

            context = {
                "msg": "New entry added successfully",
                "username": username
            }
            return redirect('userPage')
        else:
            context = {
                "msg": "Please check the checkbox"
            }
            return render(request,"safe/insert.html",context)

    else:
        context = {
            "msg": "Invalid request method"
        }
        return render(request,"safe/insert.html",context)
