from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Comentario

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['nome', 'email', 'conteudo']