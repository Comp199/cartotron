from django.db import models


# Create your models here.
class Category(models.Model):
    """
    A product category within the store
    """
    name = models.CharField(max_length=25)

    # to string
    def __str__(self):
        return self.name


class Product(models.Model):
    """
    A product within the store
    """
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    categories = models.ManyToManyField(Category)
    description = models.TextField()
    sku = models.CharField(max_length=10)

    def __str__(self):
        return self.name
