
from django.forms import ModelForm
from .models import EmployeeRegModel,JobseekerApplicationFormModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class EmployeeRegistrationForm(ModelForm):
    class Meta:
        model=EmployeeRegModel
        fields= "__all__"


class EmployerRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class JobSeekerRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class JobseekerApplicationForm(ModelForm):
    class Meta:
        model = JobseekerApplicationFormModel
        fields = "__all__"
