from django.db import models
from ckeditor.fields import RichTextField

class Project(models.Model):
    title = models.CharField(max_length=200, blank=False)
    description = RichTextField()
    link = models.URLField(max_length=500, default='')

    def __str__(self):
        return self.title

class Contact(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=500)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.email

