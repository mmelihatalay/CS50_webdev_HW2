from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields import DurationField


class User(AbstractUser):
    pass


class Currency(models.Model):
    name = models.CharField(max_length=64)
    sign = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}-{self.sign}"


class Product(models.Model):
    name = models.CharField(max_length=64, blank=False)
    price = models.DecimalField(max_digits=19, decimal_places=2)
    description = models.TextField(blank=False)
    currency = models.ForeignKey(
        Currency, on_delete=models.CASCADE, related_name="currencies")
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="product_owners", blank=False)
    url = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.owner}'s {self.name} {self.currency.sign}{self.price}"


class Comment(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="products", blank=False)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comment_owners", blank=False)
    comment = models.CharField(max_length=64, blank=False)

    def __str__(self):
        return f"{self.owner} {self.product.name} {self.comment[:4]}..."


class Bid(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="bid_owners", blank=False)
    offer = models.DecimalField(max_digits=19, decimal_places=2)
    currency = models.ForeignKey(
        Currency, on_delete=models.CASCADE, related_name="bid_currencies")
