from django.http import HttpResponseRedirect
from django.shortcuts import render

from shop.forms import CheckoutForm
from shop.models import Category, Product, CartItem


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


def cart_contents(request):
    """
    Fetch a product by its id from the database and render it in a detail view
    """
    product = Product.objects.all()
    context = {'product': product}

    return render(request, "shop/cart_contents.html", context)


def cart_add(request, product_id):

    if request.method == "POST":

        product = Product.objects.get(id=product_id)
        request.cart.add_item(product)

    return HttpResponseRedirect("/cart/")


def cart_remove(request, product_id):

    if request.method == "POST":

        product = Product.objects.get(id=product_id)
        request.cart.remove_item(product)

    return HttpResponseRedirect("/cart/")


def search(request):
    if request.method == "GET":

        search_query = request.GET['q']
        product_query = list(Product.objects.all())
        products = list()

        for product in product_query:
            if search_query in product.name:
                products.append(product)

        category_query = list(Product.objects.all())
        categories = list()

        for category in category_query:
            if search_query in category.name:
                categories.append(category)

        context = {'products': products, 'categories': categories}
        return render(request, "shop/search_results.html", context)


def cart_update(request):

    if request.method == "POST":

        for item, quantity in request.POST.items():

            if item.startswith("item-"):
                quantity = int(quantity)
                item_id = int(item.split("-")[1])

                if quantity <= 0:
                    request.cart.items.filter(id=item_id).delete()

                else:

                    try:
                        cart_item = request.cart.items.get(id=item_id)
                        cart_item.quantity = quantity
                        cart_item.save()
                    except CartItem.DoesNotExist:
                        pass

    return HttpResponseRedirect("/cart/")


def checkout_step_1(request):

    if request.method == "POST":
        form = CheckoutForm(data=request.POST)

        if form.is_valid():
            pass

    else:
        form = CheckoutForm()

    context = {'form': form}

    return render(request, 'shop/checkout_step_1.html', context)


def popular_list(request):
    """
    Fetch 8 products with the lowest quantity, greater than 0, and display them on the popular page
    """
    products = Product.objects.filter(quantity__gte='1').order_by('quantity')[:8]
    context = {'products': products}

    return render(request, "shop/popular_list.html", context)
