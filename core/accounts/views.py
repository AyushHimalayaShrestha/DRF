
from rest_framework import generics
from .serializer import * #RegisterSerializer,CustomTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
# Create your views here.

class RegisterUserView( generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes =[AllowAny]

class LoginUserView(TokenObtainPairView):
    serializer_class= CustomTokenObtainPairSerializer
    permission_classes = [AllowAny]