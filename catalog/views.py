from django.views.generic import TemplateView, ListView, DetailView

from catalog.models import Product


# замена контроллера FBV на CBV
#  Новый контроллер CBV
class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(name, phone, message)
        return super().get(request, *args, **kwargs)

#  Старый контроллер FBV
# def contacts(request):
#     if request.method == 'POST':
#         # в переменной request хранится информация о методе, который отправлял пользователь
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         # а также передается информация, которую заполнил пользователь
#         print(name, phone, message)
#     return render(request, 'catalog/contacts.html')


#  Новый контроллер CBV
class ProductListView(ListView):
    """Класс для вывода страницы со всеми продуктами"""
    model = Product

#  Старый контроллер FBV
# def products_list(request):
#     """Вывод страницу со всеми продуктами"""
#     products = Product.objects.all()
#     context = {
#         'object_list': products
#     }
#     return render(request, 'catalog/products_list.html', context)


class ProductDetailView(DetailView):
    """Класс для вывода страницы с одним продуктом по pk"""
    model = Product

# def product_detail(request, pk):
#     """Вывод страницы с одним продуктом по pk"""
#
#     # Возможно использовать get, но get_object_or_404 лучше
#     # product = Product.objects.get(pk=pk)
#     product = get_object_or_404(Product, pk=pk)
#     context = {
#         'object': product
#     }
#     return render(request, 'catalog/product_detail.html', context)
