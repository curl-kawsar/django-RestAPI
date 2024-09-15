from rest_framework import serializers
from django.contrib.auth.models import User
from . import models

class PatientSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    
    class Meta:
        model = models.Patient
        fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):
    confirmed_password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirmed_password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        username = validated_data['username']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        password = validated_data['password']
        password2 = validated_data['confirmed_password']
        
        if password != password2:
            raise serializers.ValidationError({'Error': 'Passwords must match'})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'Error': 'Email already exists'})
        
        account = User(
            email=email,
            username=username,
            first_name=first_name,
            last_name=last_name,
            is_active=False  # Set is_active to False
        )
        account.set_password(password)
        account.save()
        return account
    


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        if username and password:
            user = User.objects.get(username=username)
            if user:
                if not user.check_password(password):
                    raise serializers.ValidationError({'Error': 'Invalid Password'})
            else:
                raise serializers.ValidationError({'Error': 'Invalid Username'})
        else:
            raise serializers.ValidationError({'Error': 'Username and Password are required'})
        return data