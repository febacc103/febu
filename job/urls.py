from  django.urls import path,include
from .views import index,registration,login_view,sign_out,homepage,findjob



urlpatterns=[

    path("index",index,name="index"),
    path("home",homepage,name="home"),
    path("findjob", findjob, name="findjob"),
    path("register",registration,name="register"),
    path("signin", login_view, name="login"),
    path("signout",sign_out,name="logout"),

]