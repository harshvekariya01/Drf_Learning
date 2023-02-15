from django.db import models


class student(models.Model):
    employee_name =  models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)