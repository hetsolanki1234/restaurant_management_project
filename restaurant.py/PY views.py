from rest_framework.views import APIview
from rest_framework.responce import Responce

class MenuView(APIview):
    def get(self, request):
        menu = [
            {"name": "margerita pizza", "description": "classic","price":300},
            {"name": "burger", "description": "veg","price": 49},
            {"name": "pasta", "description": "pink sauce", "price":399},
            {"name": "paneer tikka", "description": "grilled paneer with cubes", "price":299},
        ]
        return Responce(menu)

form django.shortcuts import render
from .models import MenuItem

def menu_view(request):
    items = MenuItem.objects.all()
    return render(request, "menu.html",{"items": items})

