from shop.models import Cart


class CartMiddleware(object):

    def process_request(self, request):
        """
        Fetch cart from database by session id. If it doesn't exist, create a new cart instance
        but do not save it (Yet). We will save it in as soon as an item is added to it.
        """

        try:
            cart = Cart.objects.get(session_id=request.session.session_key)

        except Cart.DoesNotExist:
            cart = Cart()
            cart.session_id = request.session.session_key
            request.session.modified = True
            request.session.save()

        request.cart = cart