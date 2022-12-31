from django.db import models
from django.utils.timezone import now
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=256)
    pub_date = models.DateTimeField(default=now)
    update_date = models.DateTimeField(default=now)
    content = models.TextField()
    img = models.ImageField(upload_to="media/", blank=True)


    def __str__(self):
        return self.title