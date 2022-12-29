from django.shortcuts import render,redirect
from .models import cart,order_info,Product
from account.models import Customer
# Create your views here.
def Dashboard(request):
    orders_info=order_info.objects.all()
    carts=cart.objects.all()
    products=Product.objects.all()
    customers=Customer.objects.all()

    total_customer=customers.count()
    total_order=orders_info.count()
    take_away=orders_info.filter(take_away="Yes").count()
    payment=orders_info.filter(complete="True").count()

    context={"orders_info":orders_info, "carts":carts, "products":products , "customers":customers , "total_customer":total_customer, "total_order":total_order , "take_away":take_away , "payment":payment }
    
    return render(request,"ordering/dashboard.html",context)



