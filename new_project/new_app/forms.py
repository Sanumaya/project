from django.forms import PasswordInput
from django import forms

from new_app.models import StudentDetail
class StudentDetailForm(forms.ModelForm):
    password = forms.CharField(widget=PasswordInput)
    class Meta:
        # fields = "__all__" - to load all fields
        fields = ("first_name", "middle_name", "last_name", "contact", "email", "password") # selective fields
        model = StudentDetail

class StudentLoginForm(forms.ModelForm):
    class Meta:
        fields = ("email", "password")
        model = StudentDetail