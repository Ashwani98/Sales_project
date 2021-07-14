from django.shortcuts import render
from .models import Item

# Create your views here.

def home(request):
    items = Item.objects.all()
    return render(request, "home.html", {"items": items})

def stock(request):
    items = Item.objects.all()
    return render(request, "stocks.html", {'items': items})

def sales(request):
    items = Item.objects.all()
    return render(request, "sales.html", {'items': items})
