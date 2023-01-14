# from ordering.models import cart
# from .models import Customer

# def cart_products(request):
    
#     customer_obj = Customer.objects.get(user=request.user)
#     return {'total_cart': cart.objects.filter(user=customer_obj,complete=False).count}