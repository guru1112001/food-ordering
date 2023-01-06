from django.shortcuts import render,redirect,get_object_or_404
from .models import cart,order_info,Product
from account.models import Customer
from .decorators import admin_only,user_only
from .forms import add_productform,cartform
from django. contrib import messages
# Create your views here.

@user_only
def menu(request):
    return render(request,"ordering/menu.html")


def breakfast(request):
    products=Product.objects.all()
    context={"products":products}
    return render(request,"ordering/breakfast.html",context)

def lunch(request):
    products=Product.objects.all()
    context={"products":products}
    return render(request,"ordering/lunch.html",context)

def todayspl(request):
    products=Product.objects.all()
    context={"products":products}
    return render(request,"ordering/todayspl.html",context)

def ProductDetailView(request,id):
    product=get_object_or_404(Product,pk=id)
    context={"product":product}
    return render(request,"ordering/ProductDetailView.html",context)

def add_to_cart(request,pk):
    customer_obj = Customer.objects.get(user=request.user)
    product = Product.objects.get(id=pk)
    order_item, created = cart.objects.get_or_create(product=product, user=customer_obj, complete=False)
    order_qs = order_info.objects.filter(customer=customer_obj, complete=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.products.filter(product__id=pk).exists():
            order_item.quantity += 1
            order_item.save()
        else:
            order.products.add(order_item)
    else:
        # ordered_date = timezone.now()
        order = order_info.objects.create(customer=customer_obj)
        order.items.add(order_item)
    return redirect("Productdetail", id=product.pk)
    # customer_obj = Customer.objects.get(user=request.user)
    # product=get_object_or_404(Product,id=pk)
    # order_item,created=cart.objects.get_or_create(product=product,user=customer_obj,complete=False)
    # order_qs=order_info.objects.get_or_create(customer=customer_obj,complete=False)
    # print("order qs : ", order_qs)
    # if order_qs:
    #     order=order_qs[0]
    #     # print("order info product : ", order_qs.product.all())
    #     if order_info.objects.filter(product=product).exists():
    #     # if order.product.filter(product__pk=product.pk).exists():
    #         order_item.quantity+=1
    #         order_item.save()
    #         messages.info(request, "This item quantity was updated.")
    #         return redirect("Productdetail", id=product.pk)
    #     else:
    #      order.product.add(order_item)
    #      messages.info(request, "This item was added to your cart.")
    #     return redirect("Productdetail", id=product.pk)
    # else:
    #     order=order_info.objects.create(customer=customer_obj)
    #     order.product.add(order_item)
    #     messages.info(request, "This item was added to your cart.")
    #     return redirect("Productdetail", id=product.pk)




    
            



    


@admin_only
def Dashboard(request):
    orders_info=order_info.objects.all()
    carts=cart.objects.all()
    products=Product.objects.all()
    customers=Customer.objects.all()

    total_customer=customers.count()
    total_order=orders_info.count()
    take_away=orders_info.filter(take_away="True").count()
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

@admin_only
def update_product(request,pk):
    product=Product.objects.get(id=pk)
    form=add_productform(instance=product)

    if request.POST:
        form=add_productform(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    context={"form":form}
    return render(request,"ordering/update_product.html",context)

@admin_only
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('view_product')

    context = {'product': product}
    return render(request, 'ordering/delete_product.html', context)

@admin_only
def customer(request,pk_test):
    customer=Customer.objects.get(id=pk_test)
    orders = customer.customer_order.all()
    order_count=orders.count()
    carts=cart.objects.all()

    context={"customer":customer,"orders":orders,"order_count":order_count,"carts":carts}
    return render(request,"ordering/customer.html",context)

@admin_only
def delete_order(request,pk,pk_test):
    orders=order_info.objects.get(id=pk)
    carts=cart.objects.get(id=pk_test)
    if request.POST:
        carts.delete()
        if request.POST.get("confirm"):
            return redirect("dashboard")
    context={"orders":orders,"carts":carts}
    return render(request,"ordering/delete_order.html",context)

@admin_only
def update_order(request,pk_test):
    order=cart.objects.get(id=pk_test)
    form=cartform(instance=order)
    if request.method=="POST":
        form=cartform(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect("dashboard")

    context={"form":form}
    return render(request,"ordering/update_order.html",context)





    



