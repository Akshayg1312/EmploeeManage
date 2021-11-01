
from django.db.models import fields
from employee.models import *
from rest_framework import serializers



class EmployeeModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model  = EmployeeModel
        fields = '__all__'

