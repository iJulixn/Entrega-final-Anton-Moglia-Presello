from django.urls import path
from app_1.views import home,mostrar_perfil, about, ingresar ,cambiar_contraseña,buscar_equipo, editar_perfil,desconectar, registar,EquipoCreateView,EquipoListView,EquipoDeleteView,EquipoUpdateView,EquipoDetailView

urlpatterns = [
    path("", home, name = "home"),
    path("Perfil/", mostrar_perfil, name = "perfil"),
    path("Sobre-Nosotros/", about, name = "about"),
    path("Editar-Perfil/", editar_perfil, name = "editar_perfil"),  
    path("Cambiar-Contraseña/", cambiar_contraseña, name = "cambiar_contraseña"),  
    path("Armar-tu-equipo/", EquipoCreateView.as_view(), name = "armar_equipo"),
    path("Buscar-Equipo/", EquipoListView.as_view(), name = "buscar_equipo"),
    path("filtrar-Equipo/",buscar_equipo , name = "filtrar_equipo"),
    path("Eliminar-Equipo/<int:pk>",EquipoDeleteView.as_view() , name = "eliminar_equipo"),
    path("Editar-Equipo/<int:pk>", EquipoUpdateView.as_view(), name = "editar_equipo"),
    path("Ver-Mas-Equipo/<int:pk>", EquipoDetailView.as_view(), name = "ver_mas_equipo"),
    path("Ingresar/", ingresar, name = "login"),
    path("Cerrar Sesion/", desconectar, name = "logout"),
    path("Registrate/", registar, name = "registrar"),

]   
