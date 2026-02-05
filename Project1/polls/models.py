from django.db import models

# Create your models here.
class user(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    # address  = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name} < {self.email} >"