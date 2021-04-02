from rest_framework import serializers
from home.models import registration

from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = registration
#         fields= ['first_name','last_name','email','birthday','gender','password']
class UserSerializer(serializers.ModelSerializer):
    print("serial")
    # repassword= serializers.CharField(write_only=True)
    class Meta:
        model = registration
        fields = ['email', 'first_name','last_name','gender','birthday','password']
        extra_kwargs = {
				'password': {'write_only': True},
		}
        def	save(self,validated_data):
            password=validated_data['password'],
            # repassword=validated_data['repassword'],
            # print(repassword)
            # if password != repassword:
            #     raise serializers.ValidationError({'password': 'Passwords must match.'})
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