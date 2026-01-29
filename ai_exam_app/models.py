from django.db import models

# Create your models here.
class Student(models.Model):
    full_name = models.CharField(max_length=100,null=True,blank=True)
    registration_number = models.CharField(max_length=50, unique=True,null=True,blank=True)
    roll_number = models.CharField(max_length=50, unique=True,null=True,blank=True)
    SEMESTER_CHOICES = [
        ('1', '1st Semester'),
        ('2', '2nd Semester'),
        ('3', '3rd Semester'),
        ('4', '4th Semester'),
        ('5', '5th Semester'),
        ('6', '6th Semester'),
        ('7', '7th Semester'),
        ('8', '8th Semester'),
    ]
    semester = models.CharField(max_length=2, choices=SEMESTER_CHOICES, null=True, blank=True)
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]   
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True, blank=True)
    department = models.CharField(max_length=100,null=True,blank=True)
    phone_no = models.CharField(max_length=15, null=True,blank=True)
    email = models.EmailField(unique=True,null=True,blank=True)
    username = models.CharField(max_length=50, unique=True,null=True,blank=True)
    password = models.CharField(max_length=128,null=True,blank=True)


class Teacher(models.Model):
    full_name = models.CharField(max_length=100,null=True,blank=True)
    employee_id = models.CharField(max_length=50, unique=True,null=True,blank=True)
    age = models.IntegerField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    department = models.CharField(max_length=100,null=True, blank=True)
    phone_no = models.CharField(max_length=15,null=True, blank=True)
    email = models.EmailField(unique=True,null=True, blank=True)
    username = models.CharField(max_length=50, unique=True,null=True,blank=True)
    password = models.CharField(max_length=128,null=True,blank=True)
    