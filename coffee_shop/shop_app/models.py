import datetime
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

    def from_wallet(self, payment):
        self.wallet -= payment
        return self.save()

    def to_wallet(self, return_money):
        self.wallet += return_money
        return self.save()
    

class Product(models.Model):
    picture = models.ImageField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=30, unique=True)
    text = models.CharField(max_length=100, blank=True, null=True)
    price = models.PositiveIntegerField(blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0)

    def minus_prod(self, amount):
        self.quantity -= amount
        return self.save()

    def plus_prod(self, amount):
        self.quantity += amount
        return self.save()


class Purchase(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, default=object)
    cnt = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    to_return = models.BooleanField(default=False, blank=True, null=True)
    returned = models.BooleanField(default=False, blank=True, null=True)

    def check_cnt_available(self):
        return self.product.quantity >= self.cnt

    def is_returnable(self):
        return True
            # datetime.timedelta(minutes=3) > datetime.datetime.now() - self.create_at
