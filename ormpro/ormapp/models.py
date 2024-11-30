from django.db import models
from django.contrib import admin
class Customer (models.Model):
    cid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    salary=models.IntegerField()
    age=models.IntegerField()
    email=models.EmailField()
 
class CustomerAdmin(admin.ModelAdmin):
    list_display=('cid','name','salary','age','email')