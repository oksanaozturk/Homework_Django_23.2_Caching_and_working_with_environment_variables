from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import (ContactsTemplateView, ProductCreateView,
                           ProductDeleteView, ProductDetailView,
                           ProductListView, ProductUpdateView)

app_name = CatalogConfig.name

urlpatterns = [
    # Путь для вывода всего списка продуктов
    path("", ProductListView.as_view(), name="products_list"),
    # Путь для вывода страницы с Контактами
    path("contacts/", ContactsTemplateView.as_view(), name="contacts"),
    # Путь для вывода одного продукта
    path("product/<int:pk>/", cache_page(60)(ProductDetailView.as_view()), name="product_detail"),
    # Путь для вывода страницы при создании нового объекта
    path("product/", ProductCreateView.as_view(), name="create"),
    # Путь для вывода страницы редактирования продукта
    path("product/<int:pk>/update/", ProductUpdateView.as_view(), name="update"),
    # Путь для вывода страницы c удалением продукта
    path("product/<int:pk>/delete/", ProductDeleteView.as_view(), name="delete"),
]
