from django.shortcuts import render,redirect
from actividadclase.models import proyecto
from . import forms


def inicio(request):
    return render (request,'actividadclase/index.html')


def proyectodata(request):
    proyectos=proyecto.objects.all()
    data={'proyectos':proyectos}
    return render(request,'actividadclase/listado1.html',data)

def registrar(request):
    form = forms.registrar()  # Inicializa el formulario antes del bloque if

    if request.method == 'POST':
        form = forms.registrar(request.POST)  # Actualiza la instancia del formulario
        if form.is_valid():
            # Procesar los datos del formulario aquí
            print("form es valido")
            print("Nombre: ", form.cleaned_data['nombre'])
            print("Fecha Inicio: ", form.cleaned_data['fecha_inicio'])
            print("Fecha Termino: ", form.cleaned_data['fecha_termino'])  # Asegúrate de que esta línea sea correcta
            print("Responsable: ", form.cleaned_data['responsable'])
            print("Prioridad: ", form.cleaned_data['prioridad'])
            # Aquí puedes guardar el proyecto en la base de datos si deseas
            # Crear una nueva instancia del modelo proyecto y guardarla
            nuevo_proyecto = proyecto(
                nombre=form.cleaned_data['nombre'],
                fecha_inicio=form.cleaned_data['fecha_inicio'],
                fecha_termino=form.cleaned_data['fecha_termino'],
                responsable=form.cleaned_data['responsable'],
                prioridad=form.cleaned_data['prioridad']
            )

            nuevo_proyecto.save()
            return redirect('/listado1')   # Guarda el proyecto en la base de datos

    data = {'form': form}
    return render(request, 'actividadclase/agregar.html', data)

def eliminarProyecto(request, id):
    proyecto_instance = proyecto.objects.get(id=id)
    proyecto_instance.delete()  # Elimina el proyecto
    return redirect('/listado1')  







# Create your views here.
