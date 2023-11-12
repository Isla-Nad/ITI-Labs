from django.urls import path
from products.views import ProductEdit, ProductList, ProductCreate, ProductDelete, ProductView

urlpatterns = [
    path('list', ProductList.as_view(), name='products.list'),
    path('create', ProductCreate.as_view(), name='products.create'),
    path('delete/<int:id>/', ProductDelete.as_view(), name='products.delete'),
    path('view/<int:id>/', ProductView.as_view(), name='products.view'),
    path('edit/<int:id>/', ProductEdit.as_view(), name='products.edit'),
]
