import json

from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        """Получаем данные из фикстуры с категориями"""

        with open("fixture/catalog_category.json", "r", encoding="UTF-8") as file:
            categories = json.load(file)
            return categories

    @staticmethod
    def json_read_products():
        """Получаем данные из фикстуры с с продуктами"""

        with open("fixture/catalog_product.json", "r", encoding="UTF-8") as file:
            products = json.load(file)
            return products

    def handle(self, *args, **options):

        # Удалите все продукты
        Product.objects.all().delete()

        # Удалите все категории
        Category.objects.all().delete()

        # Создайте списки для хранения объектов
        product_for_create = []
        category_for_create = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_for_create.append(
                Category(
                    pk=category["pk"],
                    name=category["fields"].get("name"),
                    description=category["fields"].get("description"),
                )
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for product in Command.json_read_products():
            product_for_create.append(
                Product(
                    name=product["fields"].get("name"),
                    description=product["fields"].get("description"),
                    preview=product["fields"].get("preview"),
                    # получаем категорию из базы данных для корректной связки объектов
                    category=Category.objects.get(pk=product["fields"].get("category")),
                    price=product["fields"].get("price"),
                )
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)
