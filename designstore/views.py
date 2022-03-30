from django.shortcuts import render

# Create your views here.
def designstore(request):
    context = {}
    return render(request, 'designstore/designstore.html', context)
