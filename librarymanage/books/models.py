from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)
    no_of_pages = models.IntegerField()
    available = models.IntegerField()
