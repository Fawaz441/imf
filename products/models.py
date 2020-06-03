from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

PRODUCT_CATEGORY = (
    ("SMALL","Small package"),
    ("JUMBO", "Jumbo package"),
)

class Product(models.Model):
    item = models.CharField(max_length=100)
    price = models.FloatField()
    discount = models.FloatField(null=True,blank=True)
    image = models.ImageField(upload_to='products')
    category = models.CharField(max_length=10,choices = PRODUCT_CATEGORY)
    slug = models.SlugField(blank=True,null=True)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.item

    def save(self,*args, **kwargs):
        self.slug = slugify(self.item)
        super().save(*args, **kwargs)


    def detail(self):
        return reverse('products:detail',kwargs={'slug':self.slug})

    def get_price(self):
        if self.discount:
            return self.price - self.discount
        else:
            return self.price

class OrderedProduct(models.Model):
    item = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)  ##remember to set null#
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)

    def get_normal_total_price(self):
        return self.item.price * self.quantity
    
    def get_total_discounted_price(self):
        if self.item.discount:
            return self.item.get_price() * self.quantity

    def get_final_price(self):
        if self.item.discount:
            return self.get_total_discounted_price()
        else:
            return self.get_normal_total_price()

        
    def str(self):
        return "{} of {}".format(self.quantity,self.item.item)


class Order(models.Model):
    order_items = models.ManyToManyField(OrderedProduct)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    delivered = models.BooleanField(default=False)
    refunded = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)
    im_reference_code = models.CharField(max_length=20,null=True,blank=True)
    amount_paid = models.CharField(max_length=400,null=True,blank=True)
    ordered=models.BooleanField(default=False)
    pay_on_delivery = models.BooleanField(default=False)
    paystack_reference_code = models.CharField(null=True,blank=True,max_length=100)
    delivery_location = models.CharField(max_length=200,null=True,blank=True)

    def get_total_order_price(self):
        total = 0
        for item in self.order_items.all():
            total+=item.get_final_price()
        return total


    def str(self):
        return self.user.username

class Address(models.Model):
    address = models.CharField(max_length=200)
    user = models.ForeignKey(User,related_name='address',on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Addresse'




