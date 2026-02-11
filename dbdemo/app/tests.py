from django.test import TestCase

# Create your tests here.


from .models import Student, UniDetails

student = Student(
    stu_name='Sunny',
    enr_num=1,
    father_name='Rajkumar',
    mother_name='Poonam',
    address='Banwasa sonipat haryana',
    phone='8307478077'
)
student.save()

uni_details = UniDetails(
    student=student,
    course='Computer Science',
    sem=6,
    section='P122'
)
uni_details.save()
