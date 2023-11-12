from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from products.models import Product
from products.form import ProductForm
from django.contrib.auth.decorators import login_required
# products = [
#     {"id": 1, "title": "bed", "image": "pic1.png", "price": 25, "instock": 2},
#     {"id": 2, "title": "chair", "image": "pic2.png", "price": 19, "instock": 5},
#     {"id": 3, "title": "sofa", "image": "pic3.png", "price": 28, "instock": 7},
#     {"id": 4, "title": "table", "image": "pic4.png", "price": 52, "instock": 3}
# ]


def index(request):
    return render(request, 'products/index.html')


# def products_list(request):
#     return render(request, 'products/products.html', context={"products": products})


# def products_profile(request, id):
#     filtered_product = filter(lambda std: std['id'] == id, products)
#     filtered_product = list(filtered_product)
#     if filtered_product:
#         print(filtered_product[0])
#         return render(request, 'products/product_details.html', context={"product": filtered_product[0]})

#     return HttpResponse("No such student Student ")


def products_list(request):
    products = Product.objects.all()
    return render(request, 'products/products.html', context={"products": products})


def products_profile(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'products/product_details.html', context={"product": product})


@login_required()
def product_delete(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    url = reverse('products.list')
    return redirect(url)


def products_search(request):
    q = request.GET.get('q', '')
    products = Product.objects.filter(title__icontains=q)
    return render(request, 'products/products_search.html', {'products': products, 'search_term': q})


@login_required()
def create(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            image = form.cleaned_data['image']
            price = form.cleaned_data['price']
            instock = form.cleaned_data['instock']
            category = form.cleaned_data['category']
            p = Product()
            p.title = title
            p.image = image
            p.price = price
            p.instock = instock
            p.category = category
            p.save()
            return redirect(p.get_show_url())

    return render(request, 'products/products_add.html', context={"form": form})


@login_required()
def product_edit(request, id):
    p = get_object_or_404(Product, id=id)

    if request.method == 'GET':
        form = ProductForm(instance=p)
        return render(request, 'products/products_add.html', {'form': form, 'id': id})

    elif request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=p)
        if form.is_valid():
            form.save()
            return redirect(p.get_show_url())
