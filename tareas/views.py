from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarea

from django.views.decorators.http import require_POST

from django.http import JsonResponse

# Lista de tareas
def listar_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'tareas/lista.html', {'tareas': tareas})

# Crear tarea
def crear_tarea(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')  # Usa get para evitar KeyError
        descripcion = request.POST.get('descripcion', '')
        
        if titulo:  # Validación de título
            tarea = Tarea(titulo=titulo, descripcion=descripcion)  # La fecha_creacion se asignará automáticamente
            tarea.save()
            return redirect('listar_tareas')
        else:
            error_message = "El título es obligatorio."
            return render(request, 'tareas/formulario.html', {'error_message': error_message})

    return render(request, 'tareas/formulario.html')

# Editar tarea
def editar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    if request.method == 'POST':
        tarea.titulo = request.POST['titulo']
        tarea.descripcion = request.POST.get('descripcion', '')
        tarea.save()
        return redirect('listar_tareas')
    return render(request, 'tareas/formulario.html', {'tarea': tarea})

# Eliminar tarea
def eliminar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    tarea.delete()
    return redirect('listar_tareas')


# Cambiar estado de la tarea
@require_POST
def cambiar_estado(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    tarea.estado = not tarea.estado  # Cambia el estado
    tarea.save()
    
    # Retornar el nuevo estado en formato JSON
    return JsonResponse({'estado': tarea.estado})
