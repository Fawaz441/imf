from django import template
register = template.Library()
from products.models import Order

@register.filter
def cart_count(user):
    if user.is_authenticated:
        qs = Order.objects.filter(user=user,ordered=False)
        if qs.exists():
            return qs[0].order_items.count()
    return 0