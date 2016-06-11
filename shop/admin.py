from django.contrib import admin
from shop.models import Category, Product, Cart, CartItem, Invoice, LineItem, Carousel

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    pass


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)
    search_fields = ('name',)
    filter_horizontal = ('categories',)


class CartAdmin(admin.ModelAdmin):
    pass


class CartItemAdmin(admin.ModelAdmin):
    pass


class LineItemInline(admin.TabularInline):
    model = LineItem
    extra = 0


class InvoiceAdmin(admin.ModelAdmin):
    inlines = (LineItemInline, )


class CarouselAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Carousel, CarouselAdmin)
