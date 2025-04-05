from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from django.contrib import messages
from apps.product.models import Product
from django.contrib.auth import authenticate, login, logout

def dashboard_view(request):
    if request.user.is_authenticated:
        context = {}
        expired_products = Product.objects.filter(status="expired")
        active_products = Product.objects.exclude(status="expired")
        products = Product.objects.all()
        # calculate cost of active and expired products 
        expired_products_cost = sum([x.price for x in expired_products])
        active_products_cost = sum([x.price for x in active_products])
        all_products_cost = sum([x.price for x in products])

        # calculate percentage for active and expired products
        expired_percent = (expired_products_cost/all_products_cost) * 100
        active_percent = (active_products_cost/all_products_cost) * 100
        
        context["expired_products_cost"] = expired_products_cost
        context["active_products_cost"] = active_products_cost
        context["all_products_cost"] = all_products_cost
        context["expired_percent"] = expired_percent
        context["active_percent"] = active_percent
        return render(request, "account/dashboard.html",  context=context)
    else:
        return redirect("account:login")

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('account:dashboard')
        else:
            messages.error(request, "Invalid email or password")
    return render(request, 'account/login.html')

def logout_view(request):
    logout(request)
    return redirect('account:login')

