from django.db import models


# Create your models here. Database
class Category(models.Model):
    """
    A product category within the store
    """
    name = models.CharField(max_length=25)

    class Meta:
        verbose_name_plural = 'Categories'

    # to string
    def __str__(self):
        return self.name


class Product(models.Model):
    """
    A product within the store
    """
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    categories = models.ManyToManyField(Category)
    description = models.TextField()
    sku = models.CharField(max_length=10)
    image = models.ImageField(upload_to='products/images/', null=True, blank=True)

    def __str__(self):
        return self.name


class Cart(models.Model):

    session_id = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.session_id


class CartItem(models.Model):

    product = models.ForeignKey('Product')
    cart = models.ForeignKey('Cart', related_name='items')
    quantity = models.PositiveIntegerField()


class Invoice(models.Model):

    created_date = models.DateTimeField(auto_now_add=True)
    stripe_token = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=10)
    street_1 = models.CharField(max_length=50, verbose_name='Address 1')
    street_2 = models.CharField(max_length=50, blank=True, verbose_name='Address 2')
    name_first = models.CharField(max_length=30)
    name_last = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    shipping = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return '%s %s' %(self.name_first, self.name_last)


class LineItem(models.Model):

    invoice = models.ForeignKey('Invoice', related_name='line_items')
    product = models.ForeignKey('Product', blank=True, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sku = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()




