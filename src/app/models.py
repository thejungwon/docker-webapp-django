from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField('date published')
    photo = models.ImageField(upload_to='images/')
