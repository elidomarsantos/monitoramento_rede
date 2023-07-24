from django.urls import path
from django.contrib import admin
from . import views



urlpatterns = [
    path('', views.home),
    path('lista_equipamentos/', views.equipment_list),
    path('add_equipamentos/', views.add_equipamentos),
    path('editar_equipamentos/<int:id>', views.editar_equipamentos),
    path('deletar_equipamentos/<int:id>', views.deletar_equipamentos),
]

