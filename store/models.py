import types
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import proxy
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


from ecommerce import settings



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



class User(AbstractUser):

    class Types(models.TextChoices):
        CUSTOMER = 'CUSTOMER', 'Customer'
        INSTRUCTOR = "INSTRUCTOR", "Instructor"
        DRIVERS = "DRIVERS", "Drivers"

    type =models.CharField(
        _('Type'),max_length=50, choices=Types.choices, default=Types.CUSTOMER)

    #first name and last name do not cover name patterns 
    #around the globne 
    name = models.CharField(_("Name of User"), blank=True , max_length=255)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

class Customer(User):
    class Meta:
        proxy = True

class Instructor(User):
    class Meta:
        proxy = True

class Drivers(User):
    class Meta:
        proxy = True


