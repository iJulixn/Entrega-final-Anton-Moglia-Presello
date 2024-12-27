from django.urls import path
from .views import enviar_mensaje, bandeja_entrada

urlpatterns = [
    
    path('enviar-mensaje/', enviar_mensaje, name="enviar_mensaje"),
    path('bandeja-entrada/', bandeja_entrada, name="bandeja_entrada"),
]