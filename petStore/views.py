from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout
from .models import *

# Create your views here.
def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    return render(request, 'index.html', {'products':products , "categories":categories})

def product(request, id):
    product = Product.objects.get(id=id)

    products = Product.objects.filter(category=product.category).exclude(id=id)[:4]

    return render(request, 'product.html', { 'product': product, 'products': products })

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            # the authentication was successful, we can sign in the user.
            auth.login(request, user)
            return redirect('home')
        
    return render(request, 'login.html')

def register_user(request):
    if request.POST:
        # Get the user information from the form
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST['email']
        password = request.POST['password']
        exists = User.objects.filter(username=email).exists()

        if exists:
            return render(request, "register.html", {"msg": "This username already exists"})

        data = User.objects.create_user(first_name=firstname, last_name=lastname, password=password, username=email)
        data.save()

        return redirect('login')
    return render(request, 'register.html')

def logout_user(request):
    logout(request)
    return redirect("home")

def create_product(request):
    categories = Category.objects.all()
    return render(request, "create_product.html", {"categories": categories})

def category(request, id):
    categories = Category.objects.all()
    products = Product.objects.all()

    if id =='all': 
        return render (request , "category.html" , { "categories":categories , "products":products })

    for category in categories:
        product_count = Product.objects.filter(category = category).count()
        category.product_count = product_count


    products = Product.objects.filter(category = id)

    return render(request, "category.html", {"categories": categories, "products": products})

def about(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    return render(request, "about.html", { "categories":categories , "products":products })

def cart(request):
    cart_product = Cart.objects.all()
    categories = Category.objects.all()

    return render(request, "cart.html", { "categories":categories , "cart_product":cart_product })

def add_to_cart(request, id):
    cart_product = Cart.objects.all()
    categories = Category.objects.all()

    user = request.user
    product = Product.objects.get(id = id)
    new_cart = Cart.objects.create(user = user, product = product)
    new_cart.save()

    return render(request, "cart.html", {"categories":categories,  "cart_product":cart_product })