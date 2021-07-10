from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
# ========================================================
from django.forms import ModelForm

# Create your models here.


class EmployerRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","email","username","password1","password2"]
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control p-2"})

        }

class LoginForm(forms.Form):
    username=forms.CharField()
    password = forms.CharField()