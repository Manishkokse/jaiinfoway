from django.db import models

# Create your models here.
class Employee(models.Model):
    designation = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    mobile = models.CharField(null=True,max_length=12)
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.email
