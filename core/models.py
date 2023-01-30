from django.db import models
from django.contrib.auth.forms import User

class SignUp(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    password = models.CharField(max_length=128)
#    token = models.CharField(max_length=32, default=crypto_utils.token_alphanum16)
    otp = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

class BTUser(models.Model):
    name = models.CharField(max_length=128)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    email = models.EmailField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Books(models.Model):
    book_name = models.CharField(max_length=256)
    author = models.CharField(max_length=128)
    ISBN = models.IntegerField(default=0)


class Inventory(models.Model):
    book_id = Books.ISBN
    user_id = BTUser.email