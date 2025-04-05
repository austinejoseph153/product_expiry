from django.shortcuts import render, redirect
from django.http import HttpResponseNotAllowed
from django.contrib import messages
from pathlib import Path
import os
import requests
import json
from django.utils import timezone
from tempfile import NamedTemporaryFile
from django.contrib.auth.models import User
from django.core.files import File
from .forms import AddBatchForm, AddProductForm, AddNewUserForm
from .models import Product, Batch
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

base_dir = Path(__file__).parent.parent
base_dir = os.path.join(base_dir, "product/fixtures/")


def add_batch_form_view(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            context = {}
            batch_form = AddBatchForm(request.POST or None)
            if batch_form.is_valid():
                batch = Batch(**batch_form.cleaned_data)
                batch.save()
                messages.success(request,"Batch added successsfully")
                return redirect("product:batch_list")
            else:
                context["form"] = batch_form
                messages.error(request, "Form invalid")
                return render(request, 'product/add_batch_form.html', context=context)
        elif request.method == "GET":
            context = {}
            batch_form = AddBatchForm()
            context["form"] = batch_form
            return render(request, 'product/add_batch_form.html', context=context)
        else:
            return HttpResponseNotAllowed(["GET","POST"])
    else:
        return redirect("account:login")
    

def add_product_form_view(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            context = {}
            product_form = AddProductForm(request.POST or None, request.FILES or None)
            if product_form.is_valid():
                if Product.objects.filter(name=product_form.cleaned_data["name"]).exists():
                    messages.error(request,"product with similar name already exist")
                    context["form"] = product_form
                    return render(request, 'product/add_product_form.html', context=context)
                else:
                    product = Product(**product_form.cleaned_data)
                    # product.image = request.FILES.get("image")
                    product.save()
                    messages.success(request,"product added successfully")
                    return redirect("product:product_list")
            else:
                messages.error(request, "Invalid Form")
                context["form"] = product_form
                print(product_form.errors)
                print(request.FILES.get("image"))
                return render(request, 'product/add_product_form.html', context=context)
        elif request.method == "GET":
            context = {}
            product_form = AddProductForm()
            context["form"] = product_form
            return render(request, 'product/add_product_form.html', context=context)
        else:
            return HttpResponseNotAllowed(["GET","POST"])
    else:
        return redirect("account:login")

def product_list_view(request):
    if request.user.is_authenticated:
        context = {}
        products = Product.objects.all().order_by("-id")
        page_num = request.GET.get('page', 1)
        paginator = Paginator(products, 5)
        
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)

        context["product_list"] = page_obj
        return render(request, 'product/product_list.html', context=context)
    else:
        return redirect("account:login")

def batch_list_view(request):
    if request.user.is_authenticated:
        context = {}
        batches = Batch.objects.all().order_by("-id")
        context["batch_list"] = batches
        return render(request, 'product/batch_list.html', context=context)
    else:
        return redirect("account:login")
    
def expired_product_list_view(request):
    if request.user.is_authenticated:
        context = {}
        expired_products = Product.objects.filter(status="expired")
        context["expired_product_list"] = expired_products
        return render(request, 'product/expired_product_list.html', context=context)
    else:
        return redirect("account:login")

def delete_product(request, pk):
    product = Product.objects.get(pk=pk)
    messages.success(request, "Product deleted successfully")
    return redirect("product:product_list")

def create_new_user(request):
    if request.user.is_authenticated:
        context = {}
        if request.method == "POST":
            user_form = AddNewUserForm(request.POST or None)
            if user_form.is_valid():
                # check if user with similar username already exist
                if User.objects.filter(username=user_form.cleaned_data["username"]).exists():
                    messages.error(request, "User with similar username already exist")
                    context["form"] = user_form
                    return render(request, 'account/user_register.html', context=context)
                
                # check if user with similar email already exist
                if User.objects.filter(email=user_form.cleaned_data["email"]).exists():
                    messages.error(request, "User with similar email already exist")
                    context["form"] = user_form
                    return render(request, 'account/user_register.html', context=context)
                    
                user = User(**user_form.cleaned_data)
                user.set_password(user.password)
                user.save()
                messages.success(request,"User added successfully")
                return redirect("account:dashboard")
            else:
                context["form"] = user_form
                messages.error(request, "Invalid Form")
                return render(request, 'account/user_register.html', context=context)
        else:
            user_form = AddNewUserForm()
            context["form"] = user_form
            return render(request, 'account/user_register.html', context=context)
    else:
        return redirect("account:login")


# def load_waste_products():
#     responses = []
#     count = 0
#     with open(base_dir+"products.json", "r") as file:
#         responses = json.loads(file.read())
#     for product in responses:
#         image_path = product["image"]
#         name = product["name"]
#         image_name = str(name).replace(" ","-") +".jpeg"
#         count+=1
#         if not Product.objects.filter(name=name).exists():
#             image_file = requests.get(image_path)
#             lf = NamedTemporaryFile(mode="w+b")
#             lf.write(image_file.content)
#             batch = Batch.objects.get(pk=1)
#             product_instance = Product(
#                 **product
#             )
#             product_instance.image = File(lf, name=image_name)
#             product_instance.batch = batch
#             product_instance.save()
#         print(count)
# load_waste_products()