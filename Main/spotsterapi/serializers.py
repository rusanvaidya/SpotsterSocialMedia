from rest_framework import serializers
from home.models import registration

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = registration
        fields= ['first_name','last_name','email','birthday','gender','password']
