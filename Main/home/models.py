from django.db import models

# Create your models here.
class registration(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    birthday = models.CharField(max_length=50)
    gender = models.CharField(max_length=30)

class support(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=30,blank=False)
    message=models.CharField(max_length=900)

    class Meta:
        verbose_name = 'Support'
        verbose_name_plural = 'Support'