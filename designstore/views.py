from django.shortcuts import render
from . import forms

# Create your views here.
def designstore(request):
    context = {}
    return render(request, 'designstore/designstore.html', context)

def cart(request):
    context = {}
    return render(request, 'designstore/cart.html', context)


def viewitem(request):
    context = {}
    return render(request, 'designstore/viewitem.html', context)

def form_name_view(request):
    form = forms.FormName()
    #if request.method == 'POST':
    #    form = forms.FormName(request.POST)
    context = {'form': form}
    return render(request,'designstore/form_page.html', {'form': form})
