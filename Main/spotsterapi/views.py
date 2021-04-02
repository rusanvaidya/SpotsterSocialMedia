from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from home.models import registration
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token
# Create your views here.
# @api_view(['GET',])
# def user_account(request):
#     try:
#         user_info=registration.objects.all()
#         serializer = UserSerializer(user_info,many=True)
#         return JsonResponse(serializer.data,safe=False)
#     # elif request.method=='POST':
#     #     data = JSONParser().parse(request)
#     #     serializer=UserSerializer(data=data)

#     #     if serializer.is_valid():
#     #         serializer.save()
#     #         return JsonResponse(serializer.data,status=201)
#     #     return JsonResponse(serializer.errors,status=400)
#     except registration.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST', ])
def registration_view(request):
    print("views")
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'successfully registered new user.'
            data['email'] = account.email
            data['first_name']=account.first_name
            data['last_name']=account.last_name
            data['gender']=account.gender
            data['birthday']=account.birthday
            data['password']=account.password
            # data['repassword']=account.repassword

            # token = Token.objects.get(user=account).key
            # data['token'] = token
        else:
            data = serializer.errors
        return Response(data)   