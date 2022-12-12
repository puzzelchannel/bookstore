from django.db import models
from django.urls import reverse

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[self.id])

