# HomeworkDjango 21.1 по теме FBV и CBV
* Выведение всех продуктов на главную страницу через цикл {% for product in object_list %} / {% endfor %} в файле products_list.html

* Постраничное выведение каждого продукта на отдельную страницу, через применение файла product_detail.html и контроллера product_detail (в views)

* Настойка медиафайлов через настройку путей:
  
  1) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) в catalog/ urls
        
  2) В Settings:
            MEDIA_URL = '/media/'
            MEDIA_ROOT = BASE_DIR / 'media'
     
  3) Создание папки tamplatetags, добавление в него файла my_tags  с прописыванием в нем Кастомных шаблонных тегов для отображения media  файлов
     
  4) Прописывание  шаблонных фильтров или  шаблонных тегов в шаблонах . Например: {{ product.preview | media_filter }}
     То есть чтобы можно было писать 
    <a href="{{ object.image|mymedia }}" />
     вместо 
    <a href="/media/{{ object.image }}" />
