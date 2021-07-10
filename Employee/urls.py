from django.urls import path
from django.views.generic import TemplateView
from .views import EmployeeRegisterView,home,JoblistView,Findjob,Empreg_job_updateView,JobDetailView,JobDeleteView,\
EmployerRegistrationView,LoginView,JobseekerrRegistrationView,JobseekerLoginView,febu,JobSeekerApplicationRegistrationView


urlpatterns=[
    path("",febu,name="febu"),
    path("home",home,name="home"),
    path("findjob", Findjob.as_view(), name="findjob"),
    path("empregister",EmployeeRegisterView.as_view(),name="empreg"),
    path("jobs",JoblistView.as_view(),name="list"),
    path("jobupdate/<int:pk>",Empreg_job_updateView.as_view(),name="jobupdate"),
    path("jobs/<int:pk>",JobDetailView.as_view(),name="jobdetail"),
    path("jobs/delete/<int:pk>",JobDeleteView.as_view(),name="jobdelete"),
    path("emp_reg",EmployerRegistrationView.as_view(),name="emp_reg"),
    path("login",LoginView.as_view(),name="login"),
    path("js_reg",JobseekerrRegistrationView.as_view(),name="js_reg"),
    path("js_login",JobseekerLoginView.as_view(),name="js_login"),
    path("js_application",JobSeekerApplicationRegistrationView.as_view(),name="js_application")


]