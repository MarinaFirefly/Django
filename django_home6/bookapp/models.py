from django.contrib.auth.models import AbstractUser
from django.db import models


class Customer(models.Model):
    # USERNAME_FIELD = 'username'
    username = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    is_moderator = models.NullBooleanField()

    def get_full_name(self):
        return '{} {}'.format(self.first_name,self.last_name)


class Book(models.Model):
    text = models.CharField(max_length=25)
    author = models.CharField(max_length=25)
    article = models.CharField(max_length=25)


class Comment(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
