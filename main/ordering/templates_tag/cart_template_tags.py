from django import template
from ordering. models import order_info

register = template.Library()


@register.filter
def cart_item_count(user):
    qs = order_info.objects.filter(customer=user, complete=False)
    
    return qs[0].products.count()
    