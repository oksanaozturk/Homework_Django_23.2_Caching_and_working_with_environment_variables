from django.core.cache import cache

from catalog.models import Product, Category
from config.settings import CACHE_ENABLED


def get_products_from_cache():
    """Функция для получения данных о продуктах из кеша"""
    # Проверка, что кеш работает(если настройки кеша нет, будет выводиться Product.objects.all())
    if CACHE_ENABLED:
        # Устанавливаем ключ, по которому будем получать данные из radis
        key = "products_list"
        # Обращаемся к radis  для получения данных
        products = cache.get(key)
        if products is None:
            # Если данных нет, то получаем их из БД
            products = Product.objects.all()
            # Устанавливаем полученный данные в кеш
            cache.set(key, products)

    else:
        products = Product.objects.all()

    return products


def get_category_from_cache():
    """Функция для получения данных о категориях из кеша"""

    # Проверка, что кеш работает
    if not CACHE_ENABLED:
        return Category.objects.all()

    # Устанавливаем ключ, по которому будем получать данные из radis
    key = "category_list"

    # Обращаемся к radis  для получения данных
    categories = cache.get(key)
    if categories is None:
        # Если данных нет, то получаем их из БД
        categories = Category.objects.all()
        # Устанавливаем полученный данные в кеш
        cache.set(key, categories)

    return categories
