from django.db import models
from ckeditor.fields import RichTextField

from django.db import models
from ckeditor.fields import RichTextField
from django.db import models
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200, blank=False)
    description = RichTextField()
    link = models.URLField(max_length=500, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=500)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.email

