from django import forms
from django.contrib.auth.models import User
from .models import Equipo, Perfil

class EquipoFormulario(forms.ModelForm):

    class Meta:
        model = Equipo
        fields = "__all__"

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ["first_name","last_name","email"]

class PerfilUpdateForm(forms.ModelForm):

    class Meta:
        model = Perfil
        fields = ["imagen"]

