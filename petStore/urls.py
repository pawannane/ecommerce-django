from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('product/<int:id>/', product, name='product'),
    path('login/', login_user, name='login'),
    path('register/', register_user, name='register'),
    path('logout/', logout_user, name="logout"),
    path('create/', create_product, name="create"),
    path('category/<int:id>/', category, name="category"),
    path('about/', about, name="about"),
    path('cart/', display_cart, name='display_cart'),
    path('add_to_cart/<int:id>', add_to_cart, name='add_to_cart'),  
    path('delete/<int:id>', delete_user, name='delete_product'),
    path('success/', success, name='success'),
]
