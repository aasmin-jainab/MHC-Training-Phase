from django.db import models

# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    DOB=models.DateField()
    date=models.CharField(max_length=50)
    address=models.TextField()
    def __str__(self):
        return f"{self.first_name}{self.last_name}"