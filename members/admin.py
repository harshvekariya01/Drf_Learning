from django.contrib import admin
from .models import student,Profession

# Register your models here.


class student1(admin.ModelAdmin):
    list_display = ['employee_name','roll','city']
admin.site.register(student,student1)


class Profession1(admin.ModelAdmin):
    list_display = ['name','active']
admin.site.register(Profession,Profession1)