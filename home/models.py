import datetime

from django.db import models

# Create your models here.
class registration(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    birthday = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)



class userpost(models.Model):
    author = models.ForeignKey(registration, on_delete=models.CASCADE)
    feeling = models.CharField(max_length=100,blank=True)
    emoji = models.FilePathField(blank=True)
    usercontent = models.TextField(max_length=1000,blank=True)
    userfile= models.FileField(upload_to='user_post',blank=True)
    created = models.DateTimeField(default=datetime.datetime.now)
    liked = models.ManyToManyField(registration, related_name='likes')
    # def __str__(self):
    #     return str(self.usercontent)[:50]
    class Meta:
        ordering = ('-created',)

    @property
    def num_likes(self):
        return self.liked.all().count()



LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)


class Like(models.Model):
    user = models.ForeignKey(registration, on_delete=models.CASCADE)
    post = models.ForeignKey(userpost, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, max_length=8)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return f"{self.user}-{self.post}-{self.value}"


class comment(models.Model):
    id = models.AutoField
    comments = models.TextField(blank=False,max_length=1000)
    user_id = models.IntegerField(blank=False)
    post_id = models.IntegerField(blank=False)
    created_date = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        ordering = ('-created_date',)
    
    @property
    def num_comments(self):
        return self.comment.all().count()

class support(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=30,blank=False)
    message=models.CharField(max_length=900)

    class Meta:
        verbose_name = 'Support'
        verbose_name_plural = 'Support'

class pinvalid(models.Model):
    id = models.AutoField
    email = models.EmailField(max_length=30,blank=False)
    instantpin = models.IntegerField(default=False,blank=False)
    created_time = models.DateTimeField(default=datetime.datetime.now)

    @property
    def delete_after_five_minutes(self):
        if self.created_time < datetime.datetime.now()-datetime.timedelta(minutes=2):
            e = pinvalid.objects.get(pk=self.pk)
            e.delete()
            return True
        else:
            return False
