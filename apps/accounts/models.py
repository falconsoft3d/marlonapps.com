from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager;


# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, firstname, lastname, email, password=None):
        if not email:
            raise ValueError('el usuario debe tener un email')
        
        if not username:
            raise ValueError('el usuario no tiene username')


class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50)
    
    # Campos atributos de Django
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    
    USERNAME_FILED = 'email'
    REQUIRED_FIELDS = ['username', 'firstname', 'lastname']
    
    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perm(self, add_label):
        return True