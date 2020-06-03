from django.urls import path
from .views import (product_list,add_item_to_cart,
remove_whole_from_cart,order_final,
remove_one_from_cart,product_detail,
payment_option,pay_on_delivery,use_default_address)

app_name = 'products'

urlpatterns = [
    path('',product_list,name='product'),
    path('products/<slug>/',product_detail,name='detail'),
    path('add_to_cart/<slug>',add_item_to_cart,name='add_to_cart'),
    path('remove_whole_from_cart/<slug>',remove_whole_from_cart,name='remove_whole'),
    path('order_final_summary',order_final,name='order_final'),
    path('remove_bir/<slug>',remove_one_from_cart,name='remove_one'),
    path('payment_option',payment_option,name='payment_option'),
    path('pay-on-delivery',pay_on_delivery,name='pay_on_delivery'),
    path('use_default_address',use_default_address,name='use_default'),
]


