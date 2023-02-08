from django.urls import path
from appcoder.views import *

urlpatterns = [
    
    path('cursos/', curso),
    path('', inicio, name= 'home'),
    path('profes/', profesor, name= 'profes'),
    path('cursoform/', cursoFormulario,)
    
]