from django.contrib import admin
from .models import student

# Register your models here.


class student1(admin.ModelAdmin):
    list_display = ['employee_name','roll','city']
admin.site.register(student,student1)