from rest_framework import generics
from .serializer import *
from .models import *

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

# delete category
class CategoryDeleteView(generics.DestroyAPIView):
    queryset= Category.objects.all()
    serializer_class = CategorySerializer