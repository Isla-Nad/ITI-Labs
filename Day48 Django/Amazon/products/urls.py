from django.urls import path
from products.views import products_list, products_profile, product_delete, product_edit, products_search, create

urlpatterns = [
    path('list', products_list, name='products.list'),
    path('product/<int:id>', products_profile, name='products.profile'),
    path('product/<int:id>/delete', product_delete, name='products.delete'),
    path('product/search', products_search, name='products.search'),
    path('product/form/create', create, name='products.forms.create'),
    path('product/<int:id>/edit', product_edit, name='products.edit'),
]
