from django.shortcuts import render,get_object_or_404,redirect
from .models import Product,Order,OrderedProduct,Address
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import random
from django.dispatch import receiver
from paystack.views import payment_verified
from users.forms import DeliveryForm
# Create your views here.

@login_required
def order_final(request):
    old_orders = Order.objects.filter(user=request.user,ordered=True,delivered=False)
    current_order = Order.objects.filter(user=request.user,ordered=False)
    if old_orders.exists() and current_order.exists():
        return render(request,'products/order_view.html',{'self_order':current_order[0],'old_orders':old_orders})

    elif old_orders.exists():
        old_orders = old_orders
        return render(request,'products/order_view.html',{'old_orders':old_orders})

    elif current_order.exists():
        return render(request,'products/order_view.html',{'self_order':current_order[0]})
    else:
        messages.info(request,"No item in your cart")
        return redirect('home')





def product_list(request):
    jumbo_items = Product.objects.filter(category="JUMBO")
    small_items = Product.objects.filter(category="SMALL")

    context={'jumbo_items':jumbo_items,'small_items':small_items}
    return  render(request,'products/product_list.html',context=context)

def product_detail(request,slug):
    item = get_object_or_404(Product,slug=slug)
    others = set(Product.objects.exclude(slug=slug))
    others = random.sample(others,2)
    context = {'object':item,'others':others}
    return render(request,'products/product_detail.html',context=context)
    
        

        

@login_required()
def add_item_to_cart(request,slug):
    login_url = 'users:login'
    product = get_object_or_404(Product,slug=slug)
    carted_prod,created = OrderedProduct.objects.get_or_create(item=product,user=request.user,ordered=False)
    # Checking if user has an undone order
    order_qs = Order.objects.filter(user=request.user,ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.order_items.filter(item__slug=product.slug).exists():
            carted_prod.quantity +=1
            carted_prod.save()
            messages.success(request,'You now have {} of {} in your IMcart'.format(carted_prod.quantity,carted_prod.item.item))
            return redirect('products:order_final')
        
        else:
            carted_prod.quantity = 1
            carted_prod.save()
            order.order_items.add(carted_prod)
            messages.info(request,'This item has been added to your IMcart!')
            return redirect('products:product')
    
    else:
        order = Order.objects.create(user=request.user,ordered=False)
        order.order_items.add(carted_prod)
        messages.info(request,'This item has been added to your IMcart!')
        order.save()
        return redirect('products:product')

@login_required
def remove_whole_from_cart(request,slug):
    login_redirect_url = 'users:login'

    product = get_object_or_404(Product,slug=slug)
    order_qs = Order.objects.filter(user=request.user,ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.order_items.filter(item__slug=slug).exists():
            order_item = order.order_items.filter(item__slug=slug)[0]
            order.order_items.remove(order_item)
            messages.success(request,'You have successfully removed {} from your IMcart'.format(product.item))
            return redirect('products:product')
        else:
            messages.warning(request,'This item was never in your IMcart')
            return redirect('products:product')

    else:
        messages.warning(request,'You do not have an existing order!')
        return redirect('products:product')


@login_required
def remove_one_from_cart(request,slug):
    login_redirect_url = 'users:login'
    product = get_object_or_404(Product,slug=slug)
    order_qs = Order.objects.filter(user=request.user,ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.order_items.filter(item__slug=slug).exists():
            order_item = order.order_items.filter(item__slug=slug)[0]
            if order_item.quantity > 1:
                order_item.quantity -=1
                order_item.save()
            elif order_item.quantity == 1:
                order.order_items.remove(order_item)
            return redirect("products:order_final")
        else:
            messages.warning(request,"This item is not in your IMcart! ")
            return redirect("products:order_final")
    else:
        messages.warning("You do not have an order ")
        return redirect("products:order_final")

@login_required
def payment_option(request):
    form = DeliveryForm()
    order_qs = Order.objects.filter(user=request.user,ordered=False)
    if order_qs.exists():
        user_order = order_qs[0]
        email = user_order.user.email
        amount = user_order.get_total_order_price()
    else:
        messages.warning(request,"You do not have an order please!")
        return redirect('home')
    if request.method=='POST':
        form = DeliveryForm(request.POST)
        if form.is_valid():
            delivery_location  = form.cleaned_data.get('location') +' ,' + form.cleaned_data.get('state')
            user_order.delivery_location = delivery_location
            user_order.save()
            address = Address.objects.create(user=request.user,address=delivery_location)
            return redirect('products:payment_option')
    else:
        form = DeliveryForm()


    return render(request,'products/payment_option.html',{'amount':amount,'email':email,'user_order':user_order,'form':form})




@login_required
def pay_on_delivery(request):
    order_qs = Order.objects.filter(user=request.user,ordered=False)
    if order_qs.exists():
        user_order = order_qs[0]
        user_order.pay_on_delivery = True
        user_order.ordered=True
        user_order.save()
        messages.info(request,"Your Order has been received")
        return redirect('products:order_final')
    else:
        messages.warning(request,"No order!")
        return redirect('home')

@login_required 
@receiver(payment_verified)
def on_payment_received(request,sender,ref,amount,**kwargs):
    order_qs = Order.objects.filter(user=request.user,ordered=False)
    if order_qs.exists():
        user_order = order_qs[0]
        user_order.paystack_reference_code = ref
        user_order.amount_paid = "N" + str(amount)
        user_order.ordered = True
        user_order.save()
        messages.info(request,"Payment successful")
        return redirect('products:order_final')

    else:
        messages.warning(request,"No order!")
        return redirect('home')



def use_default_address(request):
    address = Address.objects.filter(user=request.user)[0]
    order = Order.objects.filter(user=request.user,ordered=False)[0]
    order.delivery_location = address.address
    order.save()
    return redirect('products:payment_option')

