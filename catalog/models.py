from django.db import models


# Данная переменная создается для того, чтобы применять её в данных, которые можно не заполнять (оставляьб пустым)
# blank за возможность не заполнения этого поля при создании объекта, а null позволяет отображать нулевое значение в БД
NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):

    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)  # сортировка по данному параметру

    def __str__(self):
        return self.name


class Product(models.Model):

    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)  # blank=True. null=True
    preview = models.ImageField(upload_to='products_foto', verbose_name='Изображение', **NULLABLE)
    # related_name говорит об отношении один ко многим (в одной категории м.б. несколько товаров).
    # М.Б. обращаться как category.products, а не category.product_set
    # on_delete показывает, что будет отображаться в поле при удалении категории, в данном случае ноль
    category = models.ForeignKey(Category, related_name='products', on_delete=models.SET_NULL, null=True)
    price = models.IntegerField(verbose_name='Цена')
    date_of_creation = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    last_modified_date = models.DateField(auto_now=True, verbose_name='Дата изменения')

    # manufactured_at = models.DateField(auto_now=True, verbose_name='Дата производства', **NULLABEL)

    # Необходимо для отображения модели на русскорм языке в административной панели
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name',)  # сортировка по данному параметру. В кортежах и списках ставим запятую в конце!!!

    def __str__(self):
        return self.name
