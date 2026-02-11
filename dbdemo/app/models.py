from django.db import models

# Create your models here.
class Class(models.Model):
    StudentName = models.TextField()
    FatherName = models.TextField()

class Driver(models.Model):
    name = models.TextField()
    license = models.TextField()

class Car(models.Model):
    make = models.TextField()
    model = models.TextField()
    year = models.IntegerField()
    owner = models.ForeignKey(Driver, on_delete=models.CASCADE)

# class student(models.Model):
#     stu_name = models.TextField()
#     enr_num = models.IntegerField()
#     father_name = models.TextField()
#     mother_name = models.TextField()
#     address = models.TextField()
#     phone = models.IntegerField()

# class uni_details(models.Model):
#     stu_name = models.TextField()
#     enr_num = models.IntegerField()
#     course = models.TextField()
#     sem = models.IntegerField()
#     section = models.TextField()


class Student(models.Model):
    stu_name = models.CharField(max_length=100)
    enr_num = models.IntegerField(primary_key=True)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)

class UniDetails(models.Model):
    student = models.ForeignKey("Student", on_delete=models.CASCADE)
    course = models.CharField(max_length=100)
    sem = models.IntegerField()
    section = models.CharField(max_length=10)
