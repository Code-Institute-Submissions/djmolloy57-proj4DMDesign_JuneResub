from django.shortcuts import render

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
    context = {}
    return render(request,'designstore/form_page.html', context)
    