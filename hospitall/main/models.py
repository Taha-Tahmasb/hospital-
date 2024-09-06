from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price  = models.BigIntegerField()

class Transaction(models.Model):
    status = models.BooleanField(default= False)

class appointment(models.Model):
    name = models.CharField(max_length=255)
    #date = models.DateField(max_length=255)
    time = models.DateField(max_length=255)
    service = models.ForeignKey(Service)
    paying_status = models.ForeignKey(Transaction , on_delete= models.CASCADE)

