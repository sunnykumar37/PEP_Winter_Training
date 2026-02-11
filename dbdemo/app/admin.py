from django.contrib import admin

# Register your models here.
from .models import Class, Driver, Car, Student, UniDetails
admin.site.register(Class)
admin.site.register(Driver)
admin.site.register(Car)
admin.site.register(Student)
admin.site.register(UniDetails)