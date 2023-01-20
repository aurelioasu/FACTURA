from django.db import models
import datetime

class seller(models.Model):
    name = models.CharField(max_length=50, default="ConfiguroWeb")
    address = models.CharField(max_length=150, default="Cali")
    phone = models.IntegerField(default='+57 316 243 00 81')
    date = models.DateField(default=datetime.datetime.date)


class buyer(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    phone = models.IntegerField()
    purchase_date = models.DateField(default=datetime.datetime.now)


class producat(models.Model):
    img = models.ImageField(upload_to='media/')
    name = models.CharField(max_length=100)
    dis = models.TextField(max_length=500)
    price = models.CharField(max_length=100)
