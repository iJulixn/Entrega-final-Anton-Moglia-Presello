from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import CreateView,DeleteView,ListView,UpdateView,DetailView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Equipo, Perfil
from .forms import EquipoFormulario, UserUpdateForm, PerfilUpdateForm
@login_required
def mostrar_perfil(request):
    return render(request, "app_1/mostrar-perfil.html")

@login_required
def editar_perfil(request):

    usuario = request.user
    perfil, _ = Perfil.objects.get_or_create(user=usuario) 

    if request.method == "POST":
        form_usuario = UserUpdateForm(request.POST, instance = usuario)
        form_perfil = PerfilUpdateForm(request.POST, request.FILES, instance = perfil)

        if form_usuario.is_valid() and form_perfil.is_valid():  
            form_usuario.save()
            form_perfil.save()
            return redirect("perfil")
        
        else:
            return redirect("perfil")
        
    else:   
        form_usuario = UserUpdateForm(instance=usuario)
        form_perfil = PerfilUpdateForm(instance=perfil)
        
    return render(request, "app_1/forms/editar-perfil.html",{"form_usuario":form_usuario,"form_perfil":form_perfil})

@login_required
def cambiar_contraseña(request):
    if request.method == "POST":
        form_contraseña = PasswordChangeForm(request.user, request.POST)
        if form_contraseña.is_valid():
            form_contraseña.save()
            return redirect("perfil")
        else:
            return redirect("perfil")
    else:
        form_contraseña = PasswordChangeForm(request.user)
    return render(request, "app_1/forms/cambiar-contraseña.html",{"form_contraseña":form_contraseña})

def ingresar(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username= username, password = password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return redirect("home")
    else:
        return render(request, "app_1/login.html")


def desconectar(request):
    logout(request)
    return redirect("login")


def registar(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("home")
    else:
        form = UserCreationForm()
        return render(request, "app_1/registrar.html",{"form":form})


def home(request):
    return render(request, "app_1/index.html")


def about(request):
    return render(request, "app_1/about.html")


def buscar_equipo(request):

    query = request.GET.get("q")
    if query: 
        equipo = Equipo.objects.filter(juego__icontains=query)
    else:
        equipo = Equipo.objects.all()
    return render(request, "app_1/buscar_equipo.html",{"equipo":equipo})


class EquipoCreateView(LoginRequiredMixin, CreateView):
    model = Equipo
    template_name = "app_1/forms/form_crear.html"
    fields = ["juego","region","rango","cant_jugadores","objetivo"]
    success_url = reverse_lazy("buscar_equipo")


class EquipoListView(LoginRequiredMixin, ListView):

    model = Equipo
    context_object_name = "equipo"
    template_name = "app_1/buscar_equipo.html"


class EquipoDeleteView(LoginRequiredMixin, DeleteView):
    
    model = Equipo
    template_name ="app_1/forms/eliminar_form.html"
    success_url = reverse_lazy("buscar_equipo")  


class EquipoUpdateView(LoginRequiredMixin, UpdateView):
    model = Equipo
    template_name = "app_1/editar_equipo.html"
    success_url = reverse_lazy("buscar_equipo")
    fields = "__all__"  


class EquipoDetailView(LoginRequiredMixin, DetailView):
    model = Equipo
    template_name = "app_1/ver_mas.html"
