from rest_framework import serializers
from .models import StudentDetail

class StudentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDetail
        fields = ['id','first_name', 'middle_name', 'last_name','contact', 'email']