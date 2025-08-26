
from rest_framework import generics
from .serializer import RegisterSerializer
from rest_framework.permissions import AllowAny
# Create your views here.

class RegisterUserView( generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes =[AllowAny]