from rest_framework import generics
from .serializer import *
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class =CategorySerializer

# create new category
class CategoryCreateView(generics.CreateAPIView):
    queryset =Category.objects.all()
    serializer_class= CategorySerializer


# class CategoryListCreateView(generics.ListCreateAPIView):
#     queryset= Category.objects.all()
#     serializer_class= CategorySerializer

# get single category
class CategoryRetrieveView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# update category
class CategoryUpdateView(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# delete category
class CategoryDeleteView(generics.DestroyAPIView):
    queryset= Category.objects.all()
    serializer_class = CategorySerializer


# create and get all product views
class ProductCreateListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = ['category__name']
    # http://127.0.0.1:8000/api/products/?category__name =clothes
    search_fields =['name']
    # http://127.0.0.1:8000/api/products/?search = search_value
    ordering_fields=['price','created_at']
     # http://127.0.0.1:8000/api/products/?ordering = price

     # http://127.0.0.1:8000/api/products/?ordering = price & category_name= clothes


