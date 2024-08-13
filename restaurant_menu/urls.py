from django.urls import path
from . import views

urlpatterns = [
    path('', views.MenuList.as_view(), name="home"),
    path('item/<slug:slug>/', views.MenuItemDetail.as_view(), name="menu_item")
]