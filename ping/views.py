from django.shortcuts import render
from .forms import Form_Equipamentos
from django.shortcuts import redirect, render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from .models import Equipamentos
import ping3
import time

def home(request):
    
    offline = "False"
    equipments = Equipamentos.objects.filter(online=offline)
    status_offline = Equipamentos.objects.filter(online=offline).exists()
   
    

    return render(request, 'equipamentos/home.html', {"equipments": equipments, "status_offline": status_offline})
    
def equipment_list(request):
    equipments = Equipamentos.objects.order_by('-online').all()
    for equipment in equipments:
        result = ping3.ping(equipment.ip_address)
        if result is None:
            equipment.online = False
        else: 
            equipment.online = result > 0
        equipment.save()
        print(result)
       
        
    
    return render(request, 'equipamentos/lista_equipamentos.html', {'equipments': equipments})
    
def add_equipamentos(request):
    if request.method == 'POST':
        equipamentos = Form_Equipamentos(request.POST)
        if equipamentos.is_valid() :
            equipamentos.save()
            equipamentos = Form_Equipamentos()
            return redirect('/lista_equipamentos')
 
    else:
         equipamentos = Form_Equipamentos()

    return render(request, 'equipamentos/add_equipamentos.html' , {'equipamentos': equipamentos})
 
def editar_equipamentos(request, id):
    editar = get_object_or_404(Equipamentos, pk=id)
    form = Form_Equipamentos(instance=editar)
 
    if request.method == 'POST':
        form = Form_Equipamentos(request.POST, instance=editar)
         
        if form.is_valid():
            editar.save()
          
            return redirect('/lista_equipamentos')
   
        else:
            return render(request, 'equipamentos/editar_equipamentos.html', {'form':form ,'editar': editar})  


    return render(request, 'equipamentos/editar_equipamentos.html', {'form':form ,'editar': editar})  

def deletar_equipamentos(request, id):
    deletar = get_object_or_404(Equipamentos, pk=id)
   
    if request.method == 'POST':
        deletar.delete()
     
        return redirect('/lista_equipamentos')

    return render(request, 'equipamentos/deletar_equipamentos.html')
