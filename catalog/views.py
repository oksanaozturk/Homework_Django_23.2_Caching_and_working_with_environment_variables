from django.shortcuts import render, get_object_or_404
from catalog.models import Product


# def home_page(request):
#     return render(request, 'catalog/home_page.html')


def contacts(request):
    if request.method == 'POST':
        # в переменной request хранится информация о методе, который отправлял пользователь
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        # а также передается информация, которую заполнил пользователь
        print(name, phone, message)
    return render(request, 'catalog/contacts.html')


def products_list(request):
    """Вывод страницу со всеми продуктами"""
    products = Product.objects.all()
    context = {
        'object_list': products
    }
    return render(request, 'catalog/products_list.html', context)


def product_detail(request, pk):
    """Вывод страницы с одним продуктом по pk"""

    # Возможно использовать get, но get_object_or_404 лучше
    # product = Product.objects.get(pk=pk)
    product = get_object_or_404(Product, pk=pk)
    context = {
        'object': product
    }
    return render(request, 'catalog/product_detail.html', context)
