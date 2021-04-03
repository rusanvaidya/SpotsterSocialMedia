from datetime import timezone

from django.db import models

# Create your models here.
class registration(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=15)
    birthday = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)



class userpost(models.Model):
    author = models.ForeignKey(registration, on_delete=models.CASCADE)
    feeling = models.CharField(max_length=100,blank=True)
    emoji = models.FilePathField(blank=True)
    usercontent = models.TextField(max_length=1000,blank=True)
    userfile= models.FileField(upload_to='user_post',blank=True)
    created =models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return str(self.usercontent)[:50]
    class Meta:
        ordering = ('-created',)



class support(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=30,blank=False)
    message=models.CharField(max_length=900)

    class Meta:
        verbose_name = 'Support'
        verbose_name_plural = 'Support'