from django.shortcuts import render, redirect
from job.forms import EmployerRegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView,TemplateView


# Create your views here.
def homepage(request):
    return render(request, "homepage.html")

def findjob(request):
    return render(request,"findjob.html")

def index(request):
    return render(request, "index.html")


def registration(request, *args, **kwargs):
    form = EmployerRegistrationForm(request.POST)
    context = {}
    context["form"] = form
    if request.method == "POST":
        if form.is_valid():
            form.save()

            print("save")
            return redirect("login")

        else:
            print("error")

    return render(request, "registration.html", context)

def login_view(request, *arges, **kwargs):
    form = LoginForm()
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user:
                print("login success")
                login(request, user)
                return redirect("index")
            else:
                print("failed")
                context["form"] = form
    return render(request, "login.html", context)


def sign_out(request, *args, **kwargs):
    logout(request)
    return redirect("login")
