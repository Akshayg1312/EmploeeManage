# EmploeeManage

# In this I Use Django Tempalating language . and also i create Django Rest API .

# In this Project I use Django Framework and Django Templating Language

# In Project  Manage Role are register using email,password and another fields after he login then he create Employee,Edite Employe Data and  Delete Employee Data.


# I use this Technology  Django==3.2.8 ,django-dotenv==1.4.2 ,djangorestframework==3.124 ,djangorestframework-simplejwt==5.0.0

# Model for project
1) CustomUser()
2) EmployeeModel()

# Overview use in AbstractUser and manager.py file
  1) I use Manager Role For CustomUser Model .It Inherit the AbstractUser Model. It  Use because of we want add extra fields in existing User model .
  2) in this we login throught email  and default username remove
  3) In managers.py file  CustomUserManager() use for CreateSuperUser using email and password
  4) In admin.py file we register our model and change our Admin Panel design


# In Project 2 App  are there
1) employee : In this app template and models for app ,also view for that are here. In this i use django authentication .In Employee app i use boostrap,css,jquery also.

2) empAPI   : In this only API are there , in API use simple_jwt token for authentication

# .env
1) i use django-dotenv package for .env file
   in setting.py file i use the .env file data for security purpose
2) .env use for database related information and email and password hiding in smtp 

# For Manage Role :
  1)Signup
  2)Login
  3)Dashboard

    In Dashbord we show the all employee and in to corner give 1 button for add employee also delete and update butoon are gien in table.




