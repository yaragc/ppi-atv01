from django.shortcuts import render
from django.shortcuts import render, get_object_or_404,redirect
from .models import Reserva,Stand
from .forms import ReservaForm,StandForm
from  django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import messages

def index(request):
    return render(request,"reservas/index.html")
def mais(request):
    return render(request,"reservas/mais.html")
def sobre(request):
    return render(request,"reservas/sobre.html")
def cadastrar_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = ReservaForm()           
    else:
        form = ReservaForm()
    
    return render(request, "reservas/form.html", {'form':form})

def listar_reservas(request):
    reservas = Reserva.objects.all()
    context = {
        'reservas':reservas
    }
    return render (request, 'reservas/listar.html', context)


def detalhar(request, id):
    reservas = get_object_or_404(Reserva,id=id)
    context = {'reservas': reservas}
    return render(request,'reservas/detalhar.html', context)


def editar(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    
    if request.method =='POST':
        form = ReservaForm(request.POST,request.FILES,instance=reserva)
        
        if form.is_valid():
            form.save()
            return redirect('listar')
    else:
        form = ReservaForm(instance=reserva)

    return render(request,'reservas/form.html',{'form':form})
        

def apagar(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    reserva.delete()
    return redirect('listar')

