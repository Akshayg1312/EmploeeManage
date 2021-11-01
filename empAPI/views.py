from django.shortcuts import render
from django.conf import settings

from django.http import HttpResponse
from django.http import QueryDict
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status
from .serializers import *
from rest_framework import generics, permissions
from employee.models import *
from django.core.mail import send_mail
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
import dotenv
from django.db.models import Q

response =dict()

#  Signup for manager
class SignupView(generics.GenericAPIView):
    
    def post(self, request):
        if (request.data.get('email') != None and request.data.get('email') != '' and request.data.get('firstname') != None and request.data.get('firstname') != '' and request.data.get('lastname') != None and request.data.get('lastname') != '' and request.data.get('address') != None and request.data.get('address') != '' and request.data.get('dob') != None and request.data.get('dob') != '' and request.data.get('company') != None and request.data.get('company') != '' and request.data.get('password') != None and request.data.get('password') != ''):
            try:
                email = request.data.get('email')
                firstname = request.data.get('firstname')
                lastname = request.data.get('lastname')
                address = request.data.get('address')
                password = request.data.get('password')
                dob = request.data.get('dob')
                company = request.data.get('company')
                

                if CustomUser.objects.filter(email=email).exists():   # To Check email all ready exists or not

                    response['status']='false'
                    response['message'] = 'email all ready exists'
                else:

                    manager = CustomUser(email = email,first_name=firstname,last_name =lastname,address=address,dob=dob,company=company)
                    manager.set_password(password)      # to using set_password password hashed
                    manager.save()
                    response['status'] = "true"
                    response['message'] = "Manager created "
                    response['manager_id'] = manager.id
            
            except:
                response['status'] = "false"
                response['message'] = "no data found"

        else:
            response['status'] = "false"
            response['message'] = "no required param"

        return Response(response)


#  addEmployee
class AddEmplyoeeView(generics.GenericAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if (request.data.get('email') != None and request.data.get('email') != '' and request.data.get('firstname') != None and request.data.get('firstname') != '' and request.data.get('lastname') != None and request.data.get('lastname') != '' and request.data.get('address') != None and request.data.get('address') != '' and request.data.get('dob') != None and request.data.get('dob') != '' and request.data.get('city') != None and request.data.get('city') != '' and request.data.get('mobno') != None and request.data.get('mobno') != ''):
            try:

                email = request.data.get('email')
                firstname = request.data.get('firstname')
                lastname = request.data.get('lastname')
                address = request.data.get('address')
                mobno = request.data.get('mobno')
                dob = request.data.get('dob')
                city = request.data.get('city')
                

                if EmployeeModel.objects.filter(email=email).exists():   # To Check email all ready exists or not

                    response['status']='false'
                    response['message'] = 'email all ready exists'
                else:

                    emp = EmployeeModel.objects.create(email = email,firstname=firstname,lastname =lastname,address=address,dob=dob,city=city,mobile_no=mobno)
                    send_mail(                                                     # To send_mail() method use for sending mail to employee when its add using smtp 
                                    'Register Your Account',
                                    'Add your data in project',
                                    os.environ.get('EMAIL_HOST_USER'),
                                    [f'{emp.email}'],
                                    fail_silently=False,
                                )
                    response['status'] = "true"
                    response['message'] = "Manager created "
                    response['employee_id'] = emp.id
            
            except:
                response['status'] = "false"
                response['message'] = "no data found"

        else:
            response['status'] = "false"
            response['message'] = "no required param"

        return Response(response)

# update Employee
class UpdateEmployeeView(generics.GenericAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        if (request.data.get('emp_id') != None and request.data.get('emp_id') != ''):

            try:

                emp_id      = request.data.get('emp_id')
                emp         =EmployeeModel.objects.get(id = emp_id)
                
                firstname   = request.data.get('firstname',emp.firstname)
                lastname    = request.data.get('lastname',emp.lastname)
                address     = request.data.get('address',emp.address)
                mobno       = request.data.get('mobno',emp.mobile_no)
                dob         = request.data.get('dob',emp.dob)
                city        = request.data.get('city',emp.city)


                emp.firstname = firstname
                emp.lastname  = lastname
                emp.address   = address
                emp.mobile_no     = mobno
                emp.dob       = dob
                emp.city      = city

                emp.save()
                response['status'] = "true"
                response['message'] = "Employee Record updated"
                response['employee_id'] = emp_id
            except:
                response['status'] = "false"
                response['message'] = "no data found"    
            

        else:

            response['status'] = "false"
            response['message'] = "no required param"

        return Response(response)

# delete Specific employee
class DeleteEmployeebyId(generics.GenericAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if (request.data.get('emp_id') != None and request.data.get('emp_id') != ''):
        
            try:
                emp_id = request.data.get('emp_id')
                
                emp = EmployeeModel.objects.get(id =  emp_id)
                
                emp.delete()
                
                response['status'] = "true"
                response['message'] = "Emplyee deleted"
                
                
            except:
                response['status'] = "false"
                response['message'] = "no data found"

        else:
            response['status'] = "false"
            response['message'] = "no required param"

        return Response(response)

# get All Employee Record
class GetAllEmployee(generics.GenericAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
   
    def get(self, request):
    
        try:
            emp = EmployeeModel.objects.all()
            if emp.exists():
                data = EmployeeModelSerializer(emp, many=True).data
                response['status'] = "true"
                response['message'] = "data found"
                response['data'] = data
            else:
                response['status'] = "false"
                response['message'] = "no data found"
        except:
            response['status'] = "false"
            response['message'] = "no data found"


        return Response(response)


class filterapi(generics.GenericAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        if (request.data.get('word') != None ):
            word = request.POST.get('word', '0')

            lookups = Q(firstname__icontains=word) | Q(lastname__icontains=word) 

            emp =  EmployeeModel.objects.filter(lookups)
            if emp.exists():
                data = EmployeeModelSerializer(emp, many=True).data
                response['status'] = "true"
                response['message'] = "data found"
                response['data'] = data
            else:
                response['status'] = "false"
                response['message'] = "no data found"

        else:
            response['status'] = "false"
            response['message'] = "no required param"

        return Response(response)

            





