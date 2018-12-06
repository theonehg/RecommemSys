from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'shop/product/list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render(request, 'shop/product/detail.html', context)

def get_recommend_product(request):
    curr_userId = request.user.id
    cf = CF(m, 30, 1)
    cf.fit()
    list_products_id = cf.get_recommend_list(curr_userId)
    list_recom_products = []
    for product_id in list_products_id :
        product_result = Product.objects.get(id = product_id) 
        list_recom_products.append(product_result)
    context = {
        'list_recom_products' : list_recom_products
    }
    return render(request, 'shop/product/detail.html', context)   

