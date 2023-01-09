from ordering.models import cart

def cart_products(request):
    return {'total_cart': cart.objects.filter(complete=False).count}