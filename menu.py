from django.shortcuts import reader

def menu_list(request):
    menu_item = [
         {"name":"margerita","price":299}
         {"name":"burger","price":99}
    ]
    return reader(request,"menu list.html",{"menu_items":menu_items})