from django.db import models

import datetime

class chatrooms(models.Model):
    id = models.AutoField(primary_key=True)
    commuserlist = models.CharField(max_length=500, default=False)
    userroomcode = models.CharField(max_length=100, default=False)


class usermessages(models.Model):
    id = models.AutoField
    messgd = models.CharField(max_length=500)
    activeuser = models.IntegerField()
    roomcode = models.CharField(max_length=500)
    chatid = models.IntegerField()
    messagecreated = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        ordering = ('-messagecreated',)
