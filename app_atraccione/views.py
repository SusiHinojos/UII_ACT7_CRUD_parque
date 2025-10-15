from django.shortcuts import render, redirect, get_object_or_404
from .models import Atraccione

def index(request):
    atracciones = Atraccione.objects.all()
    # Asegúrate de que este nombre coincida con el nombre de tu plantilla.
    # Si la renombraste a listar_atracciones.html, está correcto.
    return render(request, 'listar_atracciones.html', {'atracciones': atracciones})

def agregar_atraccion(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        tipo = request.POST['tipo']
        capacidad = request.POST['capacidad']
        estado = request.POST['estado']
        altura_min = request.POST['altura_min']
        
        Atraccione.objects.create(
            nombre=nombre,
            tipo=tipo,
            capacidad=capacidad,
            estado=estado,
            altura_min=altura_min
        )
        return redirect('/') # Redirige al listado después de agregar
    return render(request, 'agregar.html')

def editar_atraccion(request, id):
    atraccione = get_object_or_404(Atraccione, pk=id)
    if request.method == 'POST':
        atraccione.nombre = request.POST['nombre']
        atraccione.tipo = request.POST['tipo']
        atraccione.capacidad = request.POST['capacidad']
        atraccione.estado = request.POST['estado']
        atraccione.altura_min = request.POST['altura_min']
        atraccione.save()
        return redirect('/')
    return render(request, 'editar.html', {'atraccione': atraccione})

def borrar_atraccion(request, id):
    atraccione = get_object_or_404(Atraccione, pk=id)
    if request.method == 'POST':
        atraccione.delete()
        return redirect('/')
    return render(request, 'borrar.html', {'atraccione': atraccione})