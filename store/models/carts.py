from django.db import models
from .product import Products
from .customer import Customer
import datetime


class Cart(models.Model):
    product = models.ForeignKey(Products,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    # address = models.CharField (max_length=50, default='', blank=True)
    # phone = models.CharField (max_length=50, default='', blank=True)
    date = models.DateField (default=datetime.datetime.today)
    # status = models.BooleanField (default=False)

    def placeCart(self):
        self.save()

    @staticmethod
    def get_Cart_by_customer(customer_id):
        return Cart.objects.filter(customer=customer_id).order_by('-date')

