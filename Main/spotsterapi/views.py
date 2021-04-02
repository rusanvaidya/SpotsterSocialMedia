from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from home.models import registration
from discover.models import followers
from .serializers import UserSerializer,UserLoginSerializer,UserFollowSetupSerializer
from rest_framework.authtoken.models import Token
from django.contrib import messages
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
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        data={}
        email=serializer.initial_data['email']
        if registration.objects.filter(email=email).exists():
            data['response']='Email already exists'
            data['code']='101'
        
        elif serializer.is_valid():
            account = serializer.save()
            data['response'] = 'Successfully registered new user.'
            data['email'] = account.email
            data['first_name']=account.first_name
            data['last_name']=account.last_name
            data['gender']=account.gender
            data['birthday']=account.birthday
            data['id']=account.id
            

            # token = Token.objects.get(user=account).key
            # data['token'] = token
        else:
            data = serializer.errors
        return Response(data)   

@api_view(['POST', ])
def follow_setup(request):
    if request.method=='POST':
        serializer=UserFollowSetupSerializer(data=request.data)
        data={}
        print(serializer)
        if serializer.is_valid():
            followsetup=serializer.save()
            data['response']="Saved to follower's database"
            data['user_id']=followsetup.user_id
        else:
            data=serializer.errors
        return Response(data)


@api_view(['POST',])
def login_user(request):
    if request.method == 'POST':
        serializer=UserLoginSerializer(data=request.data)
        data={}
        email=serializer.initial_data['email']
        password=serializer.initial_data['password']
        user = registration.objects.filter(email=email, password=password)
        if user.exists():
            usr_id = registration.objects.get(email=email)
            usrs_id = usr_id.id
            other = None
            my_id = None
            counts=0
            count_following =0
            

            em = followers.objects.get(user_id = usrs_id)
            other = [user_id for user_id in em.following.all()]
            count_following=len(other)
            my_id = [user_id for user_id in em.follow_me.all()]
            following_list=[]
            follower_list=[]
            for i in other:
                following_list.append(i.id)
            for i in my_id:
                follower_list.append(i.id)
            counts=len(my_id)

        if serializer.is_valid():
            data['response']='Logged in'
            data['id']=usrs_id
            data['email']=email
            data['following']=following_list
            data['followers']=follower_list
            data['follower_count']=counts
            data['following_count']=count_following
        else:
            data = serializer.errors
        return Response(data) 
 