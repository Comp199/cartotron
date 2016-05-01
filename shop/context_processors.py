from shop.models import Category



def categories(request):

    context = {}

    context["categories"] = Category.objects.all().order_by("name")

    return context