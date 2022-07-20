import re
from django.shortcuts import render

# importing forms classes
from .forms import StudentDetailForm, StudentLoginForm

# importing models
from .models import StudentDetail

# Create your views here.
def user_dashboard(request):
    context = {
        "welcome_msg": "Welcome to Information Tracker",
    }
    return render(request, "users/dashboard.html", context) 

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
    if request.method == "POST":
        std_data = StudentDetail()
        std_data.first_name = request.POST.get("first_name")
        std_data.middle_name = request.POST.get("middle_name")
        std_data.last_name = request.POST.get("last_name")
        std_data.contact = request.POST.get("contact")
        std_data.email = request.POST.get("email")
        std_data.password = request.POST.get("password")
        std_data.save()
    
        return render(request, "users/register.html", context) 