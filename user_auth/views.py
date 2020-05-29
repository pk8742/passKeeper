from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse


# Create your views here.
def user_auth(request):
    from safe.views import insert
    if not request.user.is_authenticated:
        return redirect('login_page')

    return redirect('insert')

def register_page(request):
    from safe.views import index
    context = {
        "index": index
    }
    return render(request,"user_auth/register.html",context)

def login_page(request):
    from safe.views import index
    context = {
        "index": index
    }
    return render(request,"user_auth/login.html",context)

def register_view(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        username = request.POST.get("uname")
        password = request.POST.get("pass")
        Repassword = request.POST.get("rpass")
        check = request.POST.get("check")

        if password != Repassword:
            context = {
                "msg": "Both password fields must be same"
            }
            return render(request,"user_auth/register.html",context)

        if check != "on":
            context = {
                "msg": "Please checkout the checkbox field"
            }
            return render(request,"user_auth/register.html",context)

        user = User.objects.create_user(username=username,first_name=name,email=email,password=password)
        user.save()
        context = {
            "msg": "Account created successfully"
        }
        return render(request,"user_auth/register.html",context)

def login_view(request):
    from safe.views import userPage

    username = request.POST["username"]
    password = request.POST["pass"]
    check = request.POST.get("check")
    # setting username session
    request.session['username'] = username

    if check != "on":
        context = {
            "msg": "Please checkout the checkbox field"
        }
        return render(request,"user_auth/login.html",context)

    user = authenticate(request,username=username,password=password)
    if user is not None:
        login(request,user)
        return redirect('userPage')
    else:
        context = {
            "msg": "Invalid Credentials"
        }
        return render(request,"user_auth/login.html",context)

def logout_view(request):
    logout(request)
    # username = request.session['username']
    request.session.flush()
    return render(request,"user_auth/login.html",{"msg": "logged out successfully"})
