from rest_framework.views import APIview
from rest_framework.responce import Responce

class MenuView(APIview):
    def get(self, request):
        menu = [
            {"name": "margerita pizza", "description": "classic","price":249},
            {"name": "burger", "description": "veg","price": 49},
            {"name": "pasta", "description": "pink sauce", "price":399},
            {"name": "paneer tikka", "description": "grilled paneer with cubes", "price":299},
        ]
        return Responce(menu)
