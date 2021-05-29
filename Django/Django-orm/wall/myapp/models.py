from django.db import models

class Users(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Messages(models.Model):
    message = models.TextField(null=True)
    user= models.ForeignKey(Users, related_name="users1", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Comments(models.Model):
    comment = models.TextField(null=True)
    user= models.ForeignKey(Users, related_name="users2", on_delete = models.CASCADE)
    message= models.ForeignKey(Messages, related_name="messages", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
