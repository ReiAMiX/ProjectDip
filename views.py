from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Product, CartItem, Favorite

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'shop/categories.html', {'categories': categories})


def products_by_category(request, category_id):
    products = Product.objects.filter(category_id=category_id)
    return render(request, 'shop/product_list.html', {'products': products})


@login_required
def cart(request):
    items = CartItem.objects.filter(user=request.user)
    total = sum(item.total_price() for item in items)
    return render(request, 'shop/cart.html', {'cart_items': items, 'total_price': total})


@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    CartItem.objects.get_or_create(user=request.user, product=product)
    return redirect('cart')


@login_required
def remove_from_cart(request, item_id):
    CartItem.objects.filter(id=item_id).delete()
    return redirect('cart')


@login_required
def favorites(request):
    items = Favorite.objects.filter(user=request.user)
    return render(request, 'shop/favorites.html', {'items': items})


@login_required
def add_to_favorites(request, product_id):
    product = Product.objects.get(id=product_id)
    Favorite.objects.get_or_create(user=request.user, product=product)
    return redirect('favorites')


@login_required
def remove_from_favorites(request, fav_id):
    Favorite.objects.filter(id=fav_id).delete()
    return redirect('favorites')