from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
import random
# Create your views here.
def index(request):
    if request.method=='POST':
        data = request.POST
        uname = data.get("username")
        password = data.get("password")
        
        user = authenticate(username=uname,password=password)
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
             return render(request,"index.html",{"err":"Invalid credentials"})
            
    if request.user.is_authenticated:
        return redirect("home")
        
    return render(request,"index.html")

def reg(request):
    if request.method=='POST':
        data = request.POST
        fname = data.get("firstname")
        lname = data.get("lastname")
        uname = data.get("username")
        password = data.get("password")
        
        # user = User(first_name=fname,last_name=lname,username=uname)
        # user.set_password(password)
        # user.save()
        
        User.objects.create_user(first_name=fname,last_name=lname,username=uname,password=password)
        
        return render(request,"reg.html",{"success":"Registration successfully"})
        
    return render(request,"reg.html")

@login_required(login_url="index")
def home(request):
    return render(request,"home.html")


def user_logout(request):
    logout(request)
    return redirect("index")


def forgotpass(request):
    
    try :
        if request.method=='POST':
            email = request.POST.get("email")
            action = request.POST.get("submit")
            user = User.objects.get(email=email)
            
            if action=='Send OTP':
                otp = random.randint(100,999)
                request.session['otp'] = otp
                request.session['id']=user.id
                msg = f"Your OTP is : {otp}"
                resp = "OTP sent successfully"
                send_mail(
                                "Password Recovery",
                                msg,
                                settings.EMAIL_HOST_USER,
                                [email],
                                fail_silently=False,  # Set to False to raise errors if transmission fails
                            )
                return render(request,"otpVarification.html",{"success":resp})
            else :
                msg = f"http://127.0.0.1:8000/resetpass?id={user.id}"
                resp="Link sent on registered mail"
                send_mail(
                                                "Password Recovery",
                                                msg,
                                                settings.EMAIL_HOST_USER,
                                                [email],
                                                fail_silently=False,  # Set to False to raise errors if transmission fails
                                            )
                return render(request,"forgotpass.html",{"success":resp})
            
            
           
            
            
            
            
    except User.DoesNotExist:
        return render(request,"forgotpass.html",{"err":"User Does not exist"})
    return render(request,"forgotpass.html")



def resetpass(request):
    id  =request.GET.get("id")
    if request.method=='POST':
        password = request.POST.get("password")
        user = User.objects.get(id=id)
        user.set_password(password)
        user.save()
        return redirect("index")
    return render(request,"resetpass.html")


def otpVarification(request):
    otp = int(request.GET.get("otp"))
    r_otp  =int(request.session.get("otp"))
    id = request.session.get("id")
    
    if request.method=='POST':
            password = request.POST.get("password")
            user = User.objects.get(id=id)
            user.set_password(password)
            user.save()
            return redirect("index")
    
    if(otp==r_otp):
        return render(request,"resetpass.html")
        
    else:
        return render(request,"otpVarification.html",{"err":"Invalid OTP"})