from django.contrib import admin
from django.urls import path
from employee.views import *

urlpatterns = [
    # Authentication url
    path('', dashboard, name="dashboard"),
    path('signup', signup, name="signup"),
    path('login', loginView, name="login"),
    path('logout', logout_view, name="logout"),

    # Employee url
    path('addEmployee', addEmployee, name="addEmployee"),
    path('updateEmployee', updateEmployee, name="updateEmployee"),
    path('deleteRecord', deleteRecord, name="deleteRecord"),
]