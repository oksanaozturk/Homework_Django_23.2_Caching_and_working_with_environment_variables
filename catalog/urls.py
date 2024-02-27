from django.urls import path
from catalog.views import home_page, contacts
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home_page, name='home_page'),
    path('contacts/', contacts, name='contacts')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Другой вариант прописывания media путей
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
