from django.shortcuts import render,redirect
from .models import cart,order_info,Product
from account.models import Customer
from .decorators import admin_only,user_only
from .forms import add_productform
# Create your views here.

@user_only
def menu(request):
    return render(request,"ordering/menu.html")


@admin_only
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

@admin_only
def add_product(request):
    form=add_productform()
    if request.POST:
        form=add_productform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    context = {"form": form}
    return render(request,"ordering/add_product.html",context)

@admin_only
def view_product(request):
    products=Product.objects.all()
    context={"products":products}
    return render(request,"ordering/view_product.html",context)


    



