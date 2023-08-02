from django.shortcuts import render , redirect

from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import  View
from store.models.product import Products
from store.middlewares.auth import auth_middleware

class Cart(View):
    def get(self , request):
        ids = list(request.session.get('cart').keys())
        products = Products.get_products_by_id(ids)
        print(products)
        return render(request , 'cart.html' , {'products' : products} )
    
    def post(self, request):
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Products.get_products_by_id(list(cart.keys()))
        print(customer, cart, products)

        for product in products:
            print(cart.get(str(product.id)))
            order = Cart(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          quantity=cart.get(str(product.id)))
            order.save()
        request.session['cart'] = {}

        return redirect('store')

