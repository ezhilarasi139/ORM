# Ex02 Django ORM Web Application
## Date: 12.11.2024

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM

![Screenshot 2024-11-16 113551](https://github.com/user-attachments/assets/ea6764fc-4595-4e8d-9960-98795aa617d1)


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
    eid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    salary=models.IntegerField()
    age=models.IntegerField()
    email=models.EmailField()
 
class CustomerAdmin(admin.ModelAdmin):
    list_display=('eid','name','salary','age','email')
```

## OUTPUT
![Screenshot (6)](https://github.com/user-attachments/assets/a520809c-3907-42d3-937a-6a1ac9f2ba47)



## RESULT
Thus the program for creating a database using ORM hass been executed successfully
