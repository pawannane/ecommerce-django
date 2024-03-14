from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout
from .models import *

# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def product(request, id):
    product = Product.objects.get(id=id)

    products = Product.objects.all().exclude(id=id)[:4]

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
