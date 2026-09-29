from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",index,name="index"),
    path("reg",reg,name="reg"),
    path("home",home,name="home"),
    path("logout",user_logout,name="logout"),
    
    path("forgotpass",forgotpass,name="forgotpass"),
    path("resetpass",resetpass,name="resetpass"),
    path("otpVarification",otpVarification,name="otpVarification")
]