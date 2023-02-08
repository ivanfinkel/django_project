from django.http import HttpResponse
from django.template import Template, Context, loader

def primeraVista(request):
    return HttpResponse("Vamo a juga!")

def mi_pagina(request):

   Lista = [8, 15, 19, 45, 23, 71, 15, 12, 16, 25]

   diccionario = {"argentina": "bsas", "italia": "roma", "edades": Lista }
   """
   mihtml = open("C:/Users/HP/Desktop/django_project/proyecto1/proyecto1/plantillas/pruba.html")

   plantilla = Template(mihtml.read())

   mihtml.close()

   miContexto = Context(diccionario)

   documento = plantilla.render(miContexto)
   """
   plantilla = loader.get_template("pruba.html")

   documento = plantilla.render(diccionario)

   return HttpResponse(documento)


   

