from django.urls import path
from categories.views import category_profile, categories_list, category_delete

urlpatterns = [
    path('list', categories_list, name='categories.list'),
    path('category/<int:id>', category_profile, name='category.profile'),
    path('category/<int:id>/delete', category_delete, name='category.delete'),

]
