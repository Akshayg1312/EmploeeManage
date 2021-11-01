from django.db import models

from django.contrib.auth.models import User,AbstractUser ,PermissionsMixin
from django.utils.translation import ugettext as _
from .managers import CustomUserManager




class CustomUser(AbstractUser):
    username = None
    email    = models.EmailField(_('email address'), unique = True)
    address  = models.CharField(max_length =100 ,blank=True ,null =True)
    dob      = models.DateField(null =True)
    company  = models.CharField(max_length =100 ,blank=True ,null =True)  
    USERNAME_FIELD = 'email'          #Set email as username field


    REQUIRED_FIELDS =[]
    objects = CustomUserManager()     # Create object CustomUserManager its define in Manager.py file

    def __str__(self):
        return self.email



class EmployeeModel(models.Model):
    email       =   models.EmailField( max_length = 254,unique =True)
    firstname   =   models.CharField(max_length =100)
    lastname    =   models.CharField(max_length = 100)
    address     =   models.CharField(max_length = 250)
    dob         =   models.DateField(null =True)
    mobile_no   =   models.CharField(max_length =13)
    city        =   models.CharField(max_length =50)
    created_at        = models.DateTimeField(auto_now_add=True)
    updated_at        = models.DateTimeField(auto_now=True)
    is_active         = models.IntegerField(default=1)

    def  __str__(self):
        return self.email 


