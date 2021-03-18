from django.db import models

# Create your models here.
class registration(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    birthday = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)

class support(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=30,blank=False)
    message=models.CharField(max_length=900)

    class Meta:
        verbose_name = 'Support'
        verbose_name_plural = 'Support'