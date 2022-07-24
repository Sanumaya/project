from multiprocessing import context
import re
from django.shortcuts import render
import random
import string

from django.core.mail import send_mail
# importing forms classes
from .forms import StudentDetailForm, StudentLoginForm

# importing models
from .models import StudentDetail

# Create your views here.

def generate_random_string(str_size, allowed_chars):
    return ''.join(random.choice(allowed_chars) for x in range(str_size))

def user_dashboard(request):
    context = {
        "welcome_msg": "Welcome to Information Tracker",
    }
    return render(request, "users/dashboard.html", context) 

def user_profile(request, user_id):
   data = StudentDetail.objects.get(id = user_id)
   context = {
       "db_data" : data
   }
   return render (request, "users/profile.html")

def user_edit(request, user_id):
    data = StudentDetail.objects.get(id = user_id)
    context = {"db_data" : data}
    if request.method == "POST":
        data.first_name = request.POST.get("first_name")
        data.middle_name = request.POST.get("middle_name")
        data.last_name = request.POST.get("last_name")
        data.email = request.POST.get("email")
        data.contact = request.POST.get("contact")
        data.save()
        context.setdefault("msg_success", "Updated Successfully")
        return render(request, "users/profile.html", context)
    return render(request, "users/edit.html", context)


def user_login(request):
    login_form = StudentLoginForm()
    context = {
        "form": login_form
    }
    if request.method == "POST":
        req_email = request.POST.get("email")
        req_password = request.POST.get("password")
        try:
            std_data = StudentDetail.objects.get(email=req_email)
            if std_data.password == req_password:
                return render(request, "users/dashboard.html")
            else:
                context.setdefault("msg_error", "Invalid email or password!!")
                return render(request, "users/login.html", context)
        except:
            context.setdefault("msg_error", "Invalid email or password!!")
            return render(request, "users/login.html")
    else:
        return render(request, "users/login.html", context)


def user_register(request):
    reg_form = StudentDetailForm()
    context = {
        "form": reg_form
    }
    
    chars = string.ascii_letters + string.punctuation
    size = 6
    verification_code = generate_random_string(size, chars)
    
    if request.method == "POST":
        std_data = StudentDetail()
        std_data.first_name = request.POST.get("first_name")
        std_data.middle_name = request.POST.get("middle_name")
        std_data.last_name = request.POST.get("last_name")
        std_data.contact = request.POST.get("contact")
        std_data.email = request.POST.get("email")
        std_data.password = request.POST.get("password")
        std_data.verification_code = verification_code
        std_data.save()
        
        send_mail(
            'INFO | Verification Code',
            'Your verification code is 4453' + verification_code,
            'c4crypt@gmail.com',
            [std_data.email]
         
        )
        return render(request, "users/register.html", context)
    else:
        return render(request, "users/register.html", context) 