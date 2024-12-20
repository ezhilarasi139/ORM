# Ex02 Django ORM Web Application
## Date: 14.11.2024

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM
![Screenshot 2024-12-10 140723](https://github.com/user-attachments/assets/4ab9a9c6-6acb-4ca4-b4d5-dd35ab7c9de1)



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py

from django.contrib import admin
from .models import Customer,CustomerAdmin
admin.site.register(Customer,CustomerAdmin)

models.py

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
```


## OUTPUT
![alt text](<Screenshot 2024-12-01 013746.png>)

## RESULT
Thus the program for creating a database using ORM hass been executed successfully
