from django.contrib import admin
#importing models
from .models import StudentDetail, AcademicDetail, TrainingDetail

# Register your models here.
admin.site.register(StudentDetail)
admin.site.register(AcademicDetail)
admin.site.register(TrainingDetail)

admin.site.app_index = "App_Project"
admin.site.site_header = "App_Project"
admin.site.site_title = "Admin"
admin.site.index_title = "App_Project"