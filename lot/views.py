from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Lot


def home(request):
    searchTerm = request.GET.get('searchLot')
    if searchTerm:
        lots = Lot.objects.filter(title__icontains=searchTerm)
    else:
        lots = Lot.objects.all()
    return render(request, 'home.html', {
        'name': 'Dear Guest',
        'searchTerm': searchTerm,
        'lots': lots,
    })


def detail(request, lot_id):
    lot = get_object_or_404(Lot, pk=lot_id)
    return render(request, 'detail.html', {'lot': lot})


# def signup(request):
#     email = request.GET.get('email')
#     return render(request, 'signup.html', {'email': email})


def about(request):
    return HttpResponse('<h1>This is About Us Page</h1>')
