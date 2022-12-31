from django.db import models
from django.utils.timezone import now
# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class User(models.Model):
    account = models.CharField(max_length=20)
    pw = models.CharField(max_length=20)
    
    def __str__(self):
        return self.account
