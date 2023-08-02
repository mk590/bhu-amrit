from django.contrib import admin
from django.urls import path
from .views.home import Index , store
from .views.signup import Signup
from .views.login import Login , logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .views.contact import Contact
from .middlewares.auth import  auth_middleware
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('store', store , name='store'),
    path('contact', Contact.as_view(), name='contact'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('cart', auth_middleware(Cart.as_view()) , name='carts'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),

]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
