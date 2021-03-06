from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class Peeple(AbstractUser):
    passport = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)

class Owner(models.Model):
    peeple = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthday = models.DateField()

class Auto(models.Model):
    mark = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    owners = models.ManyToManyField(Owner, through='Owning')


class Owning(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    buying_Date = models.DateField()
    selling_Date = models.DateField()


class License(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    issueDate = models.DateField()
    type = models.CharField(max_length=50)
    number = models.IntegerField()
