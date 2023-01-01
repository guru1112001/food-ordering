from django.db import models
from account.models import Customer

# Create your models here.

class Product(models.Model):
    options=(("Breakfast","Breakfast"),
    ("Lunch","Lunch"),
    ("Todayspl","Todayspl"),)
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=7,decimal_places=2)
    category=models.CharField(max_length=10,choices=options)
    description=models.TextField(max_length=500)
    image=models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.name

    
class order_info(models.Model):
    options=(("Yes","Yes"),
            ("No","No"),)
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,blank=True,related_name="customer_order")
    date_ordered=models.DateField(auto_now_add=True)
    complete=models.BooleanField(default=False)
    transaction_id=models.CharField(max_length=10)
    take_away=models.CharField(max_length=10,choices=options)

    def __str__(self):
        return self.customer.name

    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    
class cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,blank=True)
    order=models.ForeignKey(order_info,on_delete=models.SET_NULL,null=True,blank=True)
    quantity=models.IntegerField(default=0)

    def __str__(self):
        return self.product.name
    @property
    def get_total(self):

        total=self.quantity*self.product.price
        return total
