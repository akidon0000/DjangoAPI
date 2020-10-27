from django.db import models

class User(models.Model):
    #作成時刻を記録
    created = models.DateTimeField(auto_now_add=True)
    #Userの名前を記録
    name = models.CharField(max_length=100, blank=True, default='')
    #Userのemail
    mail = models.TextField()

    class Meta:
        ordering = ('created',)