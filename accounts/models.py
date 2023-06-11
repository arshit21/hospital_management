from django.db import models
from django.contrib.auth.models import User, AbstractUser
from datetime import datetime

class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    username = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    gender = models.CharField(max_length=20, blank=True)
    

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    username = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    gender = models.CharField(max_length=20, blank=True)
    department = models.CharField(max_length=100, blank=True)

class illness(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    illness = models.TextField(blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    doctor = models.ForeignKey(Staff, on_delete=models.DO_NOTHING, default=None)


class prescriptions(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    prescriptions = models.TextField(blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    doctor = models.ForeignKey(Staff, on_delete=models.DO_NOTHING, default=None)