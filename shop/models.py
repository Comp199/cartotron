from django.db import models
from tinymce import models as tinymce_models


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
    review = tinymce_models.HTMLField(blank=True)


    def __str__(self):
        return self.name


class Cart(models.Model):

    session_id = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.session_id

    def total(self):
        """
        Returns the total for all items in the cart.  If the cart does not have an id (or, it has not been
        saved to the database), no items have been added and 0 is returned.
        """
        if not self.id:
            return 0

        return 55

    def add_item(self, product):

        if not self.id:
            self.save()

        self.items.create(product=product, quantity=1)

    def remove_item(self, product):

        for instance in self.items.filter(product=product):
            instance.delete()


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




