from django.shortcuts import render, redirect
from . import forms
from .models import *
from .forms import RegisterForm

from django.contrib.auth import login, logout, authenticate

# Create your views here.
def designstore(request):
    products = Product.objects.all()
    context = { 'products':products }
    return render(request, 'designstore/designstore.html', context)

def cart(request):
    context = {}
    return render(request, 'designstore/cart.html', context)


def viewitem(request):
    context = {}
    return render(request, 'designstore/viewitem.html', context)

def form_name_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
        
            print("VALIDATION SUCCESS!")
            print("NAME: " +form.cleaned_data['name'])
            print("EMAIL: "+form.cleaned_data['email'])
            print("TEXT: "+form.cleaned_data['text'])

    return render(request,'designstore/form_page.html', {'form': form})

def viewlogo(request):
    context = {}
    return render(request, 'designstore/viewlogo.html', context)

def viewicon(request):
    context = {}
    return render(request, 'designstore/viewicon.html', context)

def sitelogin(request):
    context = {}
    #return render(request, '../account.html', context)
    return render(request, 'registration/login.html', context)

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()

    return render(request,'registration/sign_up.html', {"form": form})

