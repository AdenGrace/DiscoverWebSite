from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Area(models.Model):
    place = models.CharField("Place Name",max_length = 110)

def __str__(self):
    return self.place

class MyUsers(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email =models.EmailField('Email Adress')
def __str__(self):
    return self.first_name + ' ' + self.last_name


class Trips (models.Model):
    tripName = models.CharField('Trip Name', max_length=120)
    area = models.ForeignKey(Area, blank = True, null = True, on_delete=models.SET_NULL)
    #area = models.CharField(max_length=10)
    price = models.CharField(max_length=12)
    description = models.TextField(blank=True)
    bookings = models.ManyToManyField(MyUsers, blank= True)

def __str__(self):
    return self.tripName



