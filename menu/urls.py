from django.conf.urls import url
from django.urls import path

from . import views

app_name = "menu"

urlpatterns = [
    path('', views.menu_list, name='menu_list'),
    path('menu/item/<pk>/', views.menu_detail, name='menu_detail'),
    path('menu/new', views.create_new_menu, name='menu_new'),
    path('menu/<pk>/edit/', views.edit_menu, name='menu_edit'),
    path('menu/item/<pk>', views.item_detail, name='item_detail'),
]