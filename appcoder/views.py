from django.http import HttpResponse
from django.shortcuts import render
from appcoder.models import *

def inicio(request):
    return HttpResponse("Este es el inicio de nuestra app Agenda Familiar. Para acceder a la agenda agregue a la barra de direcciones /appcoder/listar_agenda. Para hacer un nuevo registro escriba /appcoder/crear/nombre/apellido/email/telefono/Año-Mes-Día (si el mes es marzo, escriba 3 en vez de 03)")
    
def agenda(request):
    agendas= Familia.objects.all()
    #Si quiero listarlo por la terminal, usaria un HttpResponse y usaria lo que esta abajo
    #for agenda in agendas:
        #print(agenda.nombre, agenda.apellido, agenda.email, agenda.cumpleaños, agenda.telefono)
    #return HttpResponse(agenda) 
    return render(request, "appcoder/listar_agenda.html",{'agendas':agendas})

def crear(request,nombre,apellido,email,telefono,cumpleaños) :
    persona = Familia(nombre = nombre, apellido = apellido, email = email, telefono = telefono, cumpleaños = cumpleaños)
    persona.save()
    #Esta es una forma de agregarlos desde la función pero mejor es hacerlo desde la barra de direcciones
    #persona = Familia(nombre="Rebeca", apellido="Guayurpa",email="rg@gmail.com", telefono="341155445", cumpleaños="1979-3-2")
    #persona.save()
    #persona2 = Familia(nombre="Isaac", apellido="Guayurpa",email="isaac@gmail.com", telefono="571143563", cumpleaños="1980-4-27")
    #persona2.save()
    #persona3 = Familia(nombre="Dorca", apellido="Guayurpa",email="dorca@gmail.com", telefono="12345323", cumpleaños="1977-2-24")
    #persona3.save()
    # return render(request, "appcoder/crear.html", {'persona': persona, 'persona2': persona2, 'persona3': persona3})
    return render(request, "appcoder/crear.html", {'persona': persona }) 
  


   

# Create your views here.
