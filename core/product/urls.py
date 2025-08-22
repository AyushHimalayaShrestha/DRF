from django.urls import path
from .views import *

urlpatterns =[
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/create/',CategoryCreateView.as_view(), name="create_category"),
    path('categories/<int:pk>/',CategoryRetrieveView.as_view(), name="single_category")
]