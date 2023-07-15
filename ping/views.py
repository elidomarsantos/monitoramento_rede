from django.shortcuts import render
from .forms import Form_Equipamentos
from django.shortcuts import redirect, render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from .models import Equipamentos
import ping3


def equipment_list(request):
    equipments = Equipamentos.objects.all()
    for equipment in equipments:
        result = ping3.ping(equipment.ip_address)
        equipment.is_online = result is not None
        equipment.save()
    return render(request, 'equipamentos/lista_equipamentos.html', {'equipments': equipments})
    
def add_equipamentos(request):
    if request.method == 'POST':
        equipamentos = Form_Equipamentos(request.POST)
        if equipamentos.is_valid() :
            equipamentos.save()
            equipamentos = Form_Equipamentos()
            return redirect('/')
 
    else:
         equipamentos = Form_Equipamentos()

    return render(request, 'equipamentos/add_equipamentos.html' , {'equipamentos': equipamentos})
 

