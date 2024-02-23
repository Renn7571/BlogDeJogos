from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=65,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        max_length=65,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

# for fd in LoginForm.base_fields:
#     LoginForm.base_fields[fd]

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','email','password1','password2'] 

for fd in RegisterForm.base_fields:
    RegisterForm.base_fields[fd].widget.attrs["class"] = "form-control"

