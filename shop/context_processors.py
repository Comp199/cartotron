from django.conf import settings

from shop.models import Category


def categories(request):

    context = {}

    context["categories"] = Category.objects.all().order_by("name")

    return context


def cart(request):

    context = {'cart': request.cart}
    return context


def stripe(request):

    context = {}
    context['STRIPE_PUBLISH_KEY'] = settings.STRIPE_PUBLISH_KEY

    return context