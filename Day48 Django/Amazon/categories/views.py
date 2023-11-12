from django.shortcuts import render, reverse, redirect
from categories.models import Category
from django.contrib.auth.decorators import login_required


# Create your views here.


def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'categories/categories.html', context={"categories": categories})


def category_profile(request, id):
    category = Category.objects.get(id=id)
    return render(request, 'categories/category_details.html', context={"category": category})


@login_required()
def category_delete(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    url = reverse('categories.list')
    return redirect(url)
