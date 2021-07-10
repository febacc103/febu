from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

from .forms import EmployeeRegistrationForm,EmployerRegistrationForm,JobSeekerRegistrationForm,JobseekerApplicationForm
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from .models import EmployeeRegModel

# Create your views here.
def febu(request):
    return render(request, "febu.html")
def home(request):
    return render(request,"home.html")

class Findjob(ListView):
    model=EmployeeRegModel
    template_name="findjob.html"
    context_object_name = "jobs"

class EmployeeRegisterView(CreateView):

        model = EmployeeRegModel
        form_class = EmployeeRegistrationForm
        template_name ="empregister.html"
        success_url = reverse_lazy("list")

class JoblistView(ListView):
    model=EmployeeRegModel
    template_name="listjob.html"
    context_object_name = "jobs"


class Empreg_job_updateView(UpdateView):
    template_name = "updatejob.html"
    form_class = EmployeeRegistrationForm
    model = EmployeeRegModel
    success_url = reverse_lazy("list")


# class JobDetailView(DetailView):
#     model = EmployeeRegModel
#     template_name = "jobdetail.html"

class GetObjectMixin:
    def get_object(self,id):
        return self.model.objects.get(id=id)

class JobDetailView(TemplateView,GetObjectMixin):
    model=EmployeeRegModel
    template_name = "jobdetail.html"
    context={}
    def get(self, request, *args, **kwargs):
        job=self.get_object(kwargs.get("pk"))
        self.context["job"]=job
        return render(request,self.template_name,self.context)

class JobDeleteView(DeleteView):
    model = EmployeeRegModel
    template_name = "deletejob.html"
    success_url = reverse_lazy("list")

class EmployerRegistrationView(CreateView):
    model = User
    form_class =EmployerRegistrationForm
    template_name = "emp_reg.html"
    success_url = reverse_lazy("login")


# class LoginView(TemplateView):
#     model = User
#     template_name = "login.html"
#     success_url = reverse_lazy("home")


class LoginView(TemplateView):
    model = User
    template_name = "login.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            print("success")
            login(request, user)
            return redirect("home")
        else:
            print("failed")
            return render(request, self.template_name)


class JobseekerrRegistrationView(CreateView):
    model = User
    form_class = JobSeekerRegistrationForm
    template_name = "js_reg.html"
    success_url = reverse_lazy("js_login")


class JobseekerLoginView(TemplateView):
    model = User
    template_name = "js_login.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            print("success")
            login(request, user)
            return redirect("home")
        else:
            print("failed")
            return render(request, self.template_name)


class JobSeekerApplicationRegistrationView(CreateView):
    model = EmployeeRegModel
    form_class = JobseekerApplicationForm
    template_name = "js_application.html"
    success_url = reverse_lazy("list")