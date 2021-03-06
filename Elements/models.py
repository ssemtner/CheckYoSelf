from django.db import models
from tinymce.models import HTMLField


class Product(models.Model):
    element = models.CharField(max_length=50, unique=True)
    number = models.IntegerField(unique=True)
    author = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    body = HTMLField()

    def __str__(self):
        return self.element
