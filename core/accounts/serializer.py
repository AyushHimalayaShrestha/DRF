from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields =('first_name','last_name','username','email', 'password','password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password':"Password didn't match"})
        return attrs
        
    def create(self, validated_data):
        validated_data.pop('password2')

        user =User.objects.create_user(
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            email = validated_data['email'],
            username= validated_data['username'],
            password = validated_data['password']
            )

        return user 

# custom login response        
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        data.update({
            'first_name':self.user.first_name,
            'last_name':self.user.last_name,
            'email':self.user.email,
            'username':self.user.username
        })

        return data

