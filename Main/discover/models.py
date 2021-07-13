from django.db import models

# Create your models here.
from home.models import registration


class followers(models.Model):
    user = models.OneToOneField(registration,on_delete=models.CASCADE)
    following = models.ManyToManyField(registration,related_name="Following",blank=True)
    follow_me = models.ManyToManyField(registration,related_name="Follow",blank=True)
    bio = models.CharField(default="No Bio....",max_length=5000)
    created = models.DateTimeField(auto_now_add=True)


class interest(models.Model):
    my_interest = models.CharField(max_length=200)
    interest_icon = models.ImageField(upload_to='Interest_icon',default=True)

    def __str__(self):
        return self.my_interest

class user_coordinate(models.Model):
    user=models.ForeignKey(registration,on_delete=models.CASCADE)
    latitude=models.FloatField(max_length=50,blank=True)
    longitude=models.FloatField(max_length=50,blank=True)