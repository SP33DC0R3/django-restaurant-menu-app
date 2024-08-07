from django.shortcuts import render
from django.views import generic
from .models import Items

class MenuList(generic.ListView):
    queryset = Items.objects.order_by('-date_created')
    template_name = "index.html"

class MenuItemDetail(generic.DetailView):
    model = Items
    template_name = "menu_item_details.html"