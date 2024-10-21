from django.shortcuts import render,redirect
from actividadclase.models import Proyecto
from actividadclase.forms import Registrar
#from django import index


def inicio(request):
    return render (request,'actividadclase/index.html')


def proyectodata(request):
    proyectos=Proyecto.objects.all()
    data={'proyectos':proyectos}
    return render(request,'actividadclase/listado1.html',data)

def registrarse(request):
    form = Registrar()
    if request.method=='POST':
        form=Registrar(request.POST)
        if form.is_valid():
            form.save()
        return proyectodata(request)
    data={'form':form}
    return render(request, 'actividadclase/agregar.html', data)


def eliminarProyecto(request, id):
    proyecto_instance = Proyecto.objects.get(id=id)
    proyecto_instance.delete() 
    return redirect('/listado1')  

def actualizarproyecto(request, id):
    proyecto=Proyecto.objects.get(id=id)
    form=Registrar(instance=proyecto)
    if request.method=='POST':
        form=Registrar(request.POST,instance=proyecto)
        if form.is_valid():
            form.save()
        return proyectodata(request)
    data={'form':form}
    return render(request, 'actividadclase/agregar.html',data)



# Create your views here.
