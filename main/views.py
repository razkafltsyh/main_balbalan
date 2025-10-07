import datetime
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
import json

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    context = {
        'npm' : '2406496340',
        'name': request.user.username,
        'class': 'PBP E',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }
    return render(request, "main.html", context)

def add_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "add_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.increment_views()

    context = {
        'product': product
    }
    return render(request, "product_details.html", context)

def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.all()
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'category': product.get_category_display(),
            'thumbnail': product.thumbnail,
            'product_views': product.product_views,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
            'user': product.user.username if product.user else None, 
        }
        for product in product_list
    ]

    return JsonResponse(data, safe=False)

def show_xml_by_id(request, id):
    product_item = Product.objects.filter(pk=id)
    xml_data = serializers.serialize("xml", product_item)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json_by_id(request, id):
    try:
        product = Product.objects.select_related('user').get(pk=id)

        data = {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'category': product.get_category_display(), # Mengambil nama display kategori
            'thumbnail': product.thumbnail,
            'product_views': product.product_views,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user else None,
        }
        return JsonResponse(data)
    
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return redirect('main:show_main')

@csrf_exempt
@require_POST
def add_product_ajax(request):
    name = strip_tags(request.POST.get("name"))
    price = request.POST.get("price")
    description = strip_tags(request.POST.get("description"))
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    is_featured = request.POST.get("is_featured") == 'on' 
    user = request.user

    new_product = Product(
        name=name, 
        price=price,
        description=description,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)

@csrf_exempt
@login_required
@require_POST
def delete_product_ajax(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
        if product.user != request.user:
            return HttpResponse(status=403) 
        
        product.delete()
        return HttpResponse(b"DELETED", status=200)
    except Product.DoesNotExist:
        return HttpResponse(status=404)
    
@csrf_exempt
@login_required
@require_POST
def edit_product_ajax(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
        if product.user != request.user:
            return HttpResponse(status=403) 

        product.name = strip_tags(request.POST.get("name"))
        product.price = request.POST.get("price")
        product.description = strip_tags(request.POST.get("description"))
        product.category = request.POST.get("category")
        product.thumbnail = request.POST.get("thumbnail")
        product.is_featured = request.POST.get("is_featured") == 'on'
        
        product.save()

        return HttpResponse(b"UPDATED", status=200)
    except Product.DoesNotExist:
        return HttpResponse(status=404) 

@csrf_exempt
@require_POST
def login_ajax(request):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return JsonResponse({
            'status': 'success',
            'message': 'Login successful!',
            'username': user.username
        })
    else:
        return JsonResponse({
            'status': 'error',
            'message': 'Invalid username or password.'
        }, status=400)
    
@csrf_exempt
@require_POST
def register_ajax(request):
    form = UserCreationForm(json.loads(request.body))
    if form.is_valid():
        user = form.save()
        login(request, user)
        return JsonResponse({
            'status': 'success',
            'message': 'Registration successful and logged in!'
        })
    else:
        return JsonResponse({
            'status': 'error',
            'errors': form.errors
        }, status=400)
    