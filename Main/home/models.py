from django.db import models
# from django.contrib.gis.geos import Point
# from location_field.models.plain import PlainLocationField
# Create your models here.
# For signup
class User_data(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField(default=False,primary_key=True)
    password = models.CharField(max_length=20, blank=False)
    birthday = models.DateField(blank=False)
    gender = models.CharField(max_length=10,default=False)
    profile = models.ImageField(upload_to='user_profile', blank=False,default="default_profile.jpg")

#
# class user_post(models.Model):
#     USER = models.ForeignKey(User_data, on_delete=models.CASCADE)
#     user_mind = models.CharField(max_length=1000,default="None")
#     date = models.DateTimeField(auto_now_add=True)
#     # city = models.CharField(max_length=255)
#     # p_location = PlainLocationField(based_fields=['city'], initial=Point(-49.1607606, -22.2876834),zoom=7)
#     upload_image = models.ImageField(upload_to="",default="None",blank=True)
#     # upload_video = models.