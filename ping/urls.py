from django.urls import path
from django.contrib import admin
from . import views



urlpatterns = [

    path('', views.equipment_list),
    path('add_equipamentos/', views.add_equipamentos)
]

