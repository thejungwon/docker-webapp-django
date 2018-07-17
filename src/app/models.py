from django.db import models

class Post(models.Model):
    date = models.DateTimeField('date published')
    photo = models.TextField()
