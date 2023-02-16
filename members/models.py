
from django.db import models


class student(models.Model):
    employee_name =  models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)



class Profession(models.Model):
    name =  models.CharField(max_length=100)
    active  = models.BooleanField(default=False)

    def __str__(self):
        return self.name
  
