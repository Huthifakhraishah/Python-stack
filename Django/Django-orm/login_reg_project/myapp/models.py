from django.db import models
import re
class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['username']) < 3:
            errors["username"] = " name should be at least 3 characters"
        if len(postData['passwd']) < 8:
            errors["passwd"] = "password should be at least 8 characters"
        if len(postData['address']) < 1:
            errors["address"] = "youshould enter address"
        if len(postData['email']) < 8:
            errors["email"] = "email should be at least 8 characters"
        return errors
    def basic_log(self, postData):
        errors = {}
        if len(postData['username']) < 3:
            errors["username"] = " name should be at least 3 characters"
        if len(postData['passwd']) < 8:
            errors["passwd"] = "password should be at least 8 characters"
        return errors
class User(models.Model):
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=BlogManager()