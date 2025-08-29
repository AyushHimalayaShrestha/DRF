from rest_framework import generics
from .serializer import *
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .pagination import CustomPagination
from rest_framework.permissions import AllowAny,IsAuthenticated, IsAdminUser
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class =CategorySerializer
    permission_classes = [AllowAny]

# create new category
class CategoryCreateView(generics.CreateAPIView):
    queryset =Category.objects.all()
    serializer_class= CategorySerializer
    permission_classes = [IsAdminUser]


# class CategoryListCreateView(generics.ListCreateAPIView):
#     queryset= Category.objects.all()
#     serializer_class= CategorySerializer

# get single category
class CategoryRetrieveView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]

# update category
class CategoryUpdateView(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

# delete category
class CategoryDeleteView(generics.DestroyAPIView):
    queryset= Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]


# create and get all product views
class ProductCreateListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class= CustomPagination
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = ['category__name']
    # http://127.0.0.1:8000/api/products/?category__name =clothes
    search_fields =['name']
    # http://127.0.0.1:8000/api/products/?search = search_value
    ordering_fields=['price','created_at']
     # http://127.0.0.1:8000/api/products/?ordering = price

     # http://127.0.0.1:8000/api/products/?ordering = price & category_name= clothes

    def get_permissions(self):
        if self.request.method == "GET":
           return [AllowAny()]
        return[IsAdminUser()]

