from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.
class CustomUser(AbstractUser):
    regno=models.PositiveBigIntegerField(null=True,blank=True)
    department = models.CharField(max_length=100, blank=True, null=True) 