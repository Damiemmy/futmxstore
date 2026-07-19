from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    USER_ROLE=(
        ('user','User'),
        ('admin','Admin')
    )
    username = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(unique=True)
    is_active=models.BooleanField(default=False)
    role=models.CharField(max_length=20,choices=USER_ROLE,default='user')
    is_admin=models.BooleanField(default=False)

    USERNAME_FIELD="email"
    REQUIRED_FIELDS= ["username"]

class StudentProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='student_profile')
    matric_number=models.CharField(max_length=50)
    department=models.CharField(max_length=100)
    faculty=models.CharField(max_length=100)
    level=models.IntegerField(max_length=3)
    UGT=models.CharField(max_length=10)

    def __str__(self):
        return self.user.username
