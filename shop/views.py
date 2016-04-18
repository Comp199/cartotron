from django.shortcuts import render
from shop.models import Category, Product


def category_list(request):
    """
    Fetch a all of the categories from the database in ascending order by name and render a list of categories.
    """
    categories = Category.objects.all().order_by("name")
    context = {'categories': categories}

    return render(request, "shop/category_list.html", context)


def category_detail(request, category_id):
    """
    Fetch the category and a list of products with that category from the database
     and render a list of products.
    """
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(categories=category).order_by("name")

    context = {
        'category': category,
        'products': products,
    }

    return render(request, "shop/product_list.html", context)


def product_list(request):
    """
    Fetch all of the products from the database and render them in a list
    """
    products = Product.objects.all().order_by("name")
    context = {'products': products}

    return render(request, "shop/product_list.html", context)


def product_detail(request, product_id):
    """
    Fetch a product by its id from the database and render it in a detail view
    """
    product = Product.objects.get(id=product_id)
    context = {'product': product}

    return render(request, "shop/product_detail.html", context)
