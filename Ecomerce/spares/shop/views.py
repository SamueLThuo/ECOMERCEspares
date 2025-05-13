from django.shortcuts import redirect, render
from . models import product
from . forms import ProductForm # type: ignore


def home(request):
    products_list = product.objects.all()
    return render(request, 'home.html')

def deals(request):
    products = products.objects.all()
    return render(request, 'deals.html')    

def categories(request):
    return render(request, 'categories.html') 

def contact(request):
    return render(request, 'contact.html')  

def about(request):
    return render(request, 'about.html')  

def product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    products = products.objects.all()
    return render(request, 'product.html')  

def cart_view(request):

    return render(request, 'cart.html')

def login_view(request):

    return render(request, 'login.html')

def signup_view(request):
    return render(request, 'signup.html')

