from django.db import models

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=225)
    created_at = models.DateField(auto_now_add=True)
    updated_at =  models.DateField(auto_now_add=True)


    def __str__(self):
        return self.name
    
class Student(models.Model):
    name = models.CharField(max_length=225)
    enrollment = models.CharField(max_length=20, unique=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at =  models.DateField(auto_now_add=True)


    def __str__(self):
        return self.name