from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Mensaje
# Create your views here.

@login_required
def enviar_mensaje(request): 
    if request.method == "POST":
        destinarario_username = request.POST.get("destinatario")
        contenido = request.POST.get("mensaje")
        destinatario = User.objects.get(username=destinarario_username)
        Mensaje.objects.create(remitente=request.user, destinatario=destinatario, contenido=contenido)
        return redirect("bandeja_entrada") 
    usuarios = User.objects.exclude(username=request.user.username)

    return render(request, "app_mensajeria/enviar-mensaje.html", {"usuarios":usuarios})

@login_required
def bandeja_entrada(request): 
    mensajes = Mensaje.objects.filter(destinatario=request.user).order_by("-fecha")                                                       
    return render(request, "app_mensajeria/bandeja-entrada.html", {"mensajes":mensajes})