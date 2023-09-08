from django.shortcuts import render, get_object_or_404
from .models import Category, Product

# Create your views here.
def products_in_category(request, category_slug=None):
    current_category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available_display=True)

    if category_slug:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=current_category)

    return render(request, "shot/list.html", {"current_category":current_category, "categories":categories, "products": products})

def product_in_detail(request, id, product_slug=None):
    product = get_object_or_404(Product, id, slug=product_slug)

    return render(request, "shop/detail.html", {"product":product})
