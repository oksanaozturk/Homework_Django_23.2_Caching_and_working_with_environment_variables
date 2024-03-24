from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm
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


class ProductDetailView(DetailView):
    """Класс для вывода страницы с одним продуктом по pk"""
    model = Product


class ProductCreateView(CreateView):
    model = Product
    # Добавляем формы. Заменяем fields на form_class
    # fields = ('name', 'description', 'preview', 'category', 'price')
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products_list')


class ProductUpdateView(UpdateView):
    model = Product
    # Добавляем формы. Заменяем fields на form_class
    # fields = ('name', 'description', 'preview', 'category', 'price')
    form_class = ProductForm

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.get_object().pk])
        # ранее было args=[self.kwargs.get('pk')]


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:products_list')
