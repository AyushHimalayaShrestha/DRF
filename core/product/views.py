from rest_framework import generics
from .serializer import *
from .models import *

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class =CategorySerializer