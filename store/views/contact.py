from django.shortcuts import render , redirect

from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import  View
from store.models.product import Products

class Contact(View):
    def get(self , request):
        return render(request , 'contact.html')

