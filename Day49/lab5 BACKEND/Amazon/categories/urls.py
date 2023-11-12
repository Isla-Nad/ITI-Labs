from django.urls import path
from categories.views import CategoryList, CategoryWithProducts

urlpatterns = [
    path('list', CategoryList.as_view(), name='categories.list'),
    path('view/<int:id>/', CategoryWithProducts.as_view(), name='categories.view'),

]
