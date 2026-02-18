from rest_framework.generics import ListCreateAPIView
from .models import Category, Product
from .serializers import CategorySerialzier, ProductSerialzier
from config.paginatior import MyPaginator
# Create your views here.


class CategoryListCreateApiView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerialzier
    pagination_class = MyPaginator


class ProductListCreateApiView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerialzier
    pagination_class = MyPaginator

