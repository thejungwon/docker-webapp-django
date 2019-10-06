from django.db import models


class Post(models.Model):
    date = models.DateTimeField('date published')
    photo = models.TextField()


class Pizza(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
