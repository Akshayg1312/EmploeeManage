from django.contrib import admin
from django.urls import path
from empAPI.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [

        # Manager Related API
        path('loginapi', TokenObtainPairView.as_view(), name='loginapi'),     # token generate api
        path('refresh_token', TokenRefreshView.as_view(), name='refresh_token'),
        path('signupapi', SignupView.as_view(), name="signupapi"),


        # Employee Related API
        path('addEmplyoeeapi', AddEmplyoeeView.as_view(), name="addEmplyoeeapi"),
        path('updateEmployeeapi', UpdateEmployeeView.as_view(), name="updateEmployeeapi"),
        path('deleteEmployeebyId', DeleteEmployeebyId.as_view(), name="deleteEmployeebyId"),
        path('getAllEmployee', GetAllEmployee.as_view(), name="getAllEmployee"),

        # SearchAPI
        path('getfilterapi', filterapi.as_view(), name="getfilterapi"),
        

]