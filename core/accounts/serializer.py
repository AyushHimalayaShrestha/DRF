from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(read_only=True)
    password2 = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields =('first_name','last_name','username', 'password','password2')

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
