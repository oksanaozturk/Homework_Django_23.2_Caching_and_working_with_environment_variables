from django.urls import path
from catalog.views import ContactsTemplateView, ProductListView, ProductDetailView

urlpatterns = [
    path('', ProductListView.as_view(), name='products_list'),
    # path('', home_page, name='home_page'),
    # path('contacts/', contacts, name='contacts'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail')

]
