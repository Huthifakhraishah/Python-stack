from django.db import models
from django.db.models.fields.related import ForeignKey
class Books (models.Model):
    title = models.CharField(max_length=255)
    desc=models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Authors (models.Model):
    first_name= models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    notes=models.TextField(null=True)
    books_authors=models.ManyToManyField(Books,related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)