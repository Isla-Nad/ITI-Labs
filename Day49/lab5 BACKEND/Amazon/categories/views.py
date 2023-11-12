from rest_framework.response import Response
from rest_framework.views import APIView
from categories.models import Category
from categories.serializers import CategorySerializer
from products.models import Product
from products.serializers import ProductSerializer


class CategoryList(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class CategoryWithProducts(APIView):
    def get(self, request, id):
        try:
            category = Category.objects.get(pk=id)
        except Category.DoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)

        category_serializer = CategorySerializer(category)

        products = Product.objects.filter(category=category)
        product_serializer = ProductSerializer(products, many=True)

        response_data = {
            "category": category_serializer.data,
            "products": product_serializer.data,
        }

        return Response(response_data)
