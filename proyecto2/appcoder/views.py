from django.shortcuts import render
from django.http import HttpResponse
from appcoder.models import *
from appcoder.forms import *

# Create your views here.

def inicio(request):

    return render(request, 'appcoder/inicio.html')

def curso(request):

    return render(request, 'appcoder/curso.html')

def profesor(request):

    return render(request, 'appcoder/profesor.html')

def familiar(request):

    fam1 = Familiar(parentesco= 'hermano', nombre= 'Tomas', edad= 28, fecha= '1994-04-06' )
    fam1.save()
    return HttpResponse('se ha guardado el familiar en la base de datos')

def cursoFormulario(request):
 
      if request.method == "POST":
 
            miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
            
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  curso = Curso(nombre=informacion["nombre"], camada=informacion["camada"])
                  curso.save()
                  return render(request, "appcoder/inicio.html")
      else:
            miFormulario = CursoFormulario()
 
      return render(request, "appcoder/cursoFormulario.html", {"miFormu": miFormulario})
