from django.db import models

# Create your models here.
class registration(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    birthday = birthday.fields.BirthdayField()
    gender = models.CharField(max_length=100)