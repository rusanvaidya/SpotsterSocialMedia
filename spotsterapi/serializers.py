from rest_framework import serializers
from home.models import registration
from discover.models import followers
from django.contrib import messages
from django.shortcuts import render, redirect

# from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = registration
        fields = ['email', 'first_name','last_name','gender','birthday','password']
        extra_kwargs = {
				'password': {'write_only': True},
                
		}
        def	save(self,validated_data):
            account=registration(
                    email=validated_data['email'],
                    first_name=validated_data['first_name'],
                    last_name=validated_data['last_name'],
                    gender=validated_data['gender'],
                    birthday=validated_data['birthday'],
                    password=validated_data['password'],
                    )
            account.save()
            return account
class UserFollowSetupSerializer(serializers.ModelSerializer):
    user_id=serializers.CharField()
    class Meta:
        model=followers
        fields=['user_id']
        extra_kwargs = {
				'user_id': {'read_only': False},
                
		}
        def save(self,validated_data):
            followsetup=followers(
                user_id=validated_data['user_id']
            )
            followsetup.save()
            return followsetup

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=registration
        fields=['email','password']
        extra_kwargs = {
				'password': {'write_only': True},
                
		}

    def save(self,validated_data):
        user_login_data=registration(
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user_login_data
