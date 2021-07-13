from django.db import models
from home.models import registration
# Create your models here.
class userdetails(models.Model):
    owner = models.ForeignKey(registration,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='user_profile',blank=True)
    user_bio = models.TextField(max_length=1000,blank=True)
    user_interest = models.CharField(max_length=10000,blank=True)


