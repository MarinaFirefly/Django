from django.db import models
from django.contrib.auth.models import AbstractUser


class Customer(AbstractUser):
    def __str__(self):
        return "{}".format(self.username)

    username = models.CharField(max_length=20, unique=True)
    email = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    wallet = models.PositiveIntegerField(default=1000)
    token = models.CharField(max_length=32, blank=True, null=True)


class Product(models.Model):
    picture = models.ImageField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=30, unique=True)
    text = models.CharField(max_length=100, blank=True, null=True)
    price = models.PositiveIntegerField(blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0)


class Purchase(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cnt = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)


class PurchaseReturn(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    add_for_admin = models.BooleanField(default=False)