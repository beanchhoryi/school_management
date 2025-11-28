from django.db import models

class Student(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    dob = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Subject(models.Model):
    subject_name = models.CharField(max_length=50, unique=True, null=False, blank=False)

class Teacher(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    dob = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    salary = models.DecimalField(decimal_places=2, max_digits=10)
