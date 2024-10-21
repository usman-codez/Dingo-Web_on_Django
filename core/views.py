from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import UserAuthen
from .forms import SignUp
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Udata
# Create your views here.
def index(request):
    return render(request,'core/index.html')

def blog(request):
    return render(request,'core/blog.html')

def chefs(request):
    return render(request,'core/chefs.html')

def contact(request):
    if request.method=='POST':
        fm = UserAuthen(request.POST)
        if fm.is_valid():
            mes = fm.cleaned_data['message']
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            su = fm.cleaned_data['sub']
            reg = Udata(message=mes,name=nm,email=em,sub=su)
            reg.save()

    else:
        fm = UserAuthen()
    return render(request,'core/contact.html',{'form':fm})

def sign_up(request):
    if request.method == 'POST':
        fm = SignUp(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Account created')
            fm = SignUp()
            return HttpResponseRedirect('/login/')

    else:
        fm = SignUp()
    return render(request,'core/signup.html',{'form':fm})

def log_in(request):
    if request.method=='POST':
        fm = AuthenticationForm(request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            password = fm.cleaned_data['password']
            user = authenticate(username=uname,password=password)
            login(request, user)
            return HttpResponseRedirect('/home/')
    else:
        fm = AuthenticationForm()
    return render(request,'core/login.html',{'form':fm})

def log_out(request):
    return HttpResponseRedirect('/login/')

def about(request):
    return render(request,'core/about.html')

def elements(request):
    return render(request,'core/elements.html')

def food_menu(request):
    return render(request,'core/food_menu.html')

def single_blog(request):
    return render(request,'core/single-blog.html')