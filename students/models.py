from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    matric_no = models.CharField(max_length = 50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    faculty = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    email =  models.EmailField(max_length=50)
    gpa = models.FloatField()
    
    def __str__(self):
        return (f"{self.first_name} {self.last_name}")
    