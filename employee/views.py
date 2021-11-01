from django.shortcuts import redirect, render , HttpResponse
from .models import *
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.conf import settings
from datetime import timedelta
import datetime
import time
import os
from django.db.models import Q

import json
from django.core import serializers
from django.db.models import Q , Count ,Max
from django.contrib.auth import authenticate, login,logout
from django.core.mail import send_mail




# Manager Dashboard
@login_required(login_url="/login")
def dashboard(request):

    emp = EmployeeModel.objects.all().order_by('firstname','lastname')
    context ={'emp':emp}
    return render(request,'dashboard/dashboard.html',context)

# Manager Signup
def signup(request):
    if(request.POST.get('email') != None and request.POST.get('firstname') != None and request.POST.get('lastname') != None and request.POST.get('address') != None and request.POST.get('dob') != None and request.POST.get('company') != None and  request.POST.get('password') != None):
        email = request.POST.get('email')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        address = request.POST.get('address')
        company = request.POST.get('company')
        dob = request.POST.get('dob')
        password = request.POST.get('confirmpassword')
        if CustomUser.objects.filter(email =email).exists():
            messages.warning(request,'email all ready exist')
            return redirect('signup')
        else:

            data =  CustomUser(email= email,first_name=firstname,last_name=lastname,address=address,dob=dob,company=company)
            data.set_password(password)         # to using set_password password hashed
            data.save()
            messages.success(request,f'{data.email} Manager Added Successfully')
            return redirect('signup')
        
        


    return render(request,'Manager/Signup.html')

# Manager Login
def loginView(request):
    if(request.POST.get('email') != None and request.POST.get('password') != None):
        email  =request.POST.get('email')
        password  =request.POST.get('password')

        
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
            
        else:
            return redirect('login')

    return render(request,'Manager/login.html')

# Manager Logout
def logout_view(request):
    logout(request)
    return redirect('login')


# Add Employee
def addEmployee(request):
    if request.method == 'POST':
        
        if(request.POST.get('email') != None and request.POST.get('firstname') != None and request.POST.get('lastname') != None and request.POST.get('address') != None and request.POST.get('dob') != None and request.POST.get('mobno') != None and  request.POST.get('city') != None):
            try:
                email = request.POST.get('email')
                firstname = request.POST.get('firstname')
                lastname = request.POST.get('lastname')
                address = request.POST.get('address')
                mobno = request.POST.get('mobno')
                dob = request.POST.get('dob')
                city = request.POST.get('city')

                if EmployeeModel.objects.filter(email =email).exists():
                    messages.warning(request,'email all ready exist')
                    return redirect('dashboard')
                else:

                    data =  EmployeeModel(email =email,firstname =firstname,lastname=lastname,address=address,dob=dob,mobile_no=mobno,city=city)
                    data.save()
                    
                    messages.success(request,f'{data.email} Employee Added Successfully')
                    send_mail(                                   # To send_mail() method use for sending mail to employee when its add using smtp 
                                'Register Your Account',
                                'Add your data in project',
                                os.environ.get('EMAIL_HOST_USER'),
                                [f'{data.email}'],
                                fail_silently=False,
                            )
            except:

                messages.success(request,'Something gone wrong')
                return redirect('dashboard')        
        else:

            messages.success(request,'Some Fields are Empty')
            return redirect('dashboard')        
    return redirect('dashboard')


# Update Employee
def updateEmployee(request):
    if request.method == 'POST':
        
        if(request.POST.get('email') != None and request.POST.get('firstname') != None and request.POST.get('lastname') != None and request.POST.get('address') != None and request.POST.get('dob') != None and request.POST.get('mobno') != None and  request.POST.get('city') != None):
            try:
                id = request.POST.get('id')
                emp =EmployeeModel.objects.get(id=id)
                email = request.POST.get('email')
                firstname = request.POST.get('firstname')
                lastname = request.POST.get('lastname')
                address = request.POST.get('address')
                mobno = request.POST.get('mobno')
                dob = request.POST.get('dob')
                city = request.POST.get('city')

                
                emp.firstname =firstname
                emp.lastname=lastname
                emp.address=address
                emp.dob=dob
                emp.mobile_no=mobno
                emp.city=city
                emp.save()
                messages.success(request,f'{email}  Updated Successfully')
            except:
                messages.error(request,'Something gone wrong')
                return redirect('dashboard')        
        else:
            print('in Else')
    return redirect('dashboard')


# Delete Emmployee
@login_required(login_url="/login")
def deleteRecord(request):
    if request.method == "GET":
        id = request.GET['id']
        print(id)
        try:
            emp = EmployeeModel.objects.get(id=id)
            emp.delete()
            # messages.success(request,"Empoyee Delete Successfully")
            msg = "data delete Successfully"
        except:
            msg = "Invalid Data"
        return JsonResponse(list(msg), safe=False)



