from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    no_of_pages = models.IntegerField()
    available = models.IntegerField()
    desc = models.TextField()

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)
    about = models.TextField()
    photo = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
