
from django.db import models


class student(models.Model):
    employee_name =  models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.employee_name


class Profession(models.Model):
    name =  models.CharField(max_length=100)
    roll_profrssion = models.IntegerField(null=True)
    active  = models.BooleanField(default=True)
    profession_no = models. ForeignKey(student,blank=True,null=True,on_delete=models.CASCADE)

    
    
    # def __str__(self):
    #     return self.name
    
    # @property
    # def status_message(self):
    #     if self.active:
    #         return("status activate")
    #     else:
    #         return ("status deactivate")
        
    # def num_profession_no(self):
    #     return self.profession_no.all().count()



