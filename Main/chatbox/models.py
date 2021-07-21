from django.db import models
from django.db.models.fields import AutoField
from django.db.models.fields.related import ForeignKey
import datetime
# Create your models here.

class chatroom(models.Model):
    id1 = models.AutoField
    room_name = models.CharField(max_length= 50, default=True)
    room_code = models.CharField(max_length=100, default=True)
    room_name1 = models.CharField(max_length=100, default=True)
    room_code1 = models.CharField(max_length=100, default=True)

class Messages(models.Model):
    chat_id = models.IntegerField()
    mesgd = models.CharField(max_length=500)
    active_user = models.IntegerField()
    common_user = models.CharField(max_length= 500)
    message_date = models.DateTimeField(default=datetime.datetime.now())
    chat_id2 = models.IntegerField()
    mesgd2 = models.CharField(max_length=500)
    active_user2 = models.IntegerField()
    common_user2 = models.CharField(max_length= 500)
    message_date2 = models.DateTimeField(default=datetime.datetime.now())
    
    class Meta:
        ordering = ('-message_date2',)
