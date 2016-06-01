from django.db import models
from tinymce import models as tinymce_models
from decimal import *


# Create your models here. Database
class Category(models.Model):
    """
    A product category within the store
    """
    name = models.CharField(max_length=25)
    image = models.ImageField(upload_to='category/images/', null=True, blank=True)

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
    long_description = tinymce_models.HTMLField(blank=True)

    def __str__(self):
        return self.name


class Cart(models.Model):

    session_id = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.session_id

    def subtotal(self):
        """
        Returns the subtotal for all items in the cart
        """
        amount = 0
        for item in self.items.all():
            amount += item.subtotal()
        return amount

    def tax(self):
        """
        Calculate tax.
        """
        tax = Decimal(self.subtotal() * Decimal('0.12')).quantize(Decimal('0.01'), rounding=ROUND_UP)
        # tax = Decimal(self.subtotal() * Decimal('0.12'))

        return tax

    def total(self):
        """
        Returns the total for all items in the cart.  If the cart does not have an id (or, it has not been
        saved to the database), no items have been added and 0 is returned.
        """
        if not self.id:
            return 0

        subtotal = self.subtotal()
        tax = self.tax()

        total_price = Decimal(subtotal + tax).quantize(Decimal('0.01'), rounding=ROUND_UP)

        return total_price

    def add_item(self, product, quantity=1):
        """
        Add an item to the cart. If item is already in the cart, the items quantity will be incremented by 1.
        """

        if not self.id:
            self.save()

        try:
            item = CartItem.objects.get(product=product, cart=self)
            item.quantity += quantity
            item.save()

        except CartItem.DoesNotExist:
            self.items.create(product=product, quantity=quantity)

    def remove_item(self, product):
        """
        Remove the item from the cart.
        """
        for instance in self.items.filter(product=product):
            instance.delete()

    def remove_all(self):
        """
        Remove all the items from the cart.
        """
        for instance in self.items.all():
            instance.delete()


class CartItem(models.Model):

    product = models.ForeignKey('Product')
    cart = models.ForeignKey('Cart', related_name='items')
    quantity = models.PositiveIntegerField()

    def subtotal(self):
        """
        Returns the subtotal for each individual item in the cart.
        """
        return Decimal(self.product.price * self.quantity).quantize(Decimal('0.01'), rounding=ROUND_UP)


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




