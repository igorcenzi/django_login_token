from django.db import models
from django.contrib.auth.models import AbstractUser
from .utils import CustomUserManager

# Create your models here.
class User(AbstractUser):
  email = models.EmailField(unique=True)
  password = models.CharField(max_length=100)
  
  username = None
  
  REQUIRED_FIELDS = ['password']
  USERNAME_FIELD = 'email'
  
  objects = CustomUserManager()
