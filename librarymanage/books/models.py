from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    no_of_pages = models.IntegerField()
    available = models.IntegerField()
    body = models.TextField()

    def __str__(self):
        return self.title
