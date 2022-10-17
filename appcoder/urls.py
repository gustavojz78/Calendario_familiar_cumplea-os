from django.urls import path
from appcoder.views import *

 
urlpatterns = [
    path("", inicio),
    path("listar_agenda/", agenda),
    path("crear/<str:nombre>/<str:apellido>/<str:email>/<str:telefono>/<str:cumpleaños>/", crear)
]