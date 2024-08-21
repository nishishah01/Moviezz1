from django.db import models

# Create your models here.

class Moviee(models.Model):
    title = models.CharField(max_length=255)
    year = models.CharField(max_length=10)
    genre=models.CharField(max_length=255)
    plot=models.TextField()
    poster=models.URLField()
    search=models.IntegerField(default=1)

def __str__(self):
    return self.title