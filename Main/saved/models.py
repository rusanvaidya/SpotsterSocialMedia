from django.db import models
import datetime

# Create your models here.
class user_saved_post(models.Model):
    id = models.AutoField
    user_id = models.IntegerField(blank=False)
    post_id = models.IntegerField(blank=False)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_date',)