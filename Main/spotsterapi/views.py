from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from home.models import registration
from .serializers import UserSerializer
# Create your views here.
@api_view(['GET',])
def user_account(request):
    try:
        user_info=registration.objects.all()
        serializer = UserSerializer(user_info,many=True)
        return JsonResponse(serializer.data,safe=False)
    # elif request.method=='POST':
    #     data = JSONParser().parse(request)
    #     serializer=UserSerializer(data=data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data,status=201)
    #     return JsonResponse(serializer.errors,status=400)
    except registration.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)