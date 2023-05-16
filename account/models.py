from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import customuser

# Create your models here.
#create table user(id int primary key,  first_name char(20))

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    photo = models.ImageField(upload_to="profile")

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = []

    objects = customuser()
    




    