from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    no_of_pages = models.IntegerField()
    available = models.IntegerField()
    desc = models.TextField()

    class Meta:
        ordering=['title']
    def __str__(self):
        return self.title
