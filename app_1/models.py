from django.db import models
from django.contrib.auth.models import User

class Equipo(models.Model):

    juego = models.CharField(max_length= 40)
    region = models.CharField(max_length=40)
    rango = models.CharField(max_length=40)
    cant_jugadores = models.IntegerField()
    objetivo = models.TextField()
    def __str__(self):
        return f"Juego: {self.juego} Región: {self.region} Rango: {self.rango} Cantidad de Jugadores: {self.cant_jugadores} objetivo: {self.objetivo}"
    
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="perfil_pics", null=True, blank=True)
    def __str__(self):  
        return f"{self.user.username} Perfil"