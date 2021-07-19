from itertools import chain
import requests
from django.shortcuts import render, redirect
from home.models import registration
# Create your views here.
from discover.models import followers,interest,user_location_data
from complete.models import userdetails
from json import dumps
import json
from home.models import userpost
from trending.views import get_hash_tags


import psycopg2
from psycopg2 import sql
import pandas as pd
import pandas.io.sql as sqlio
import pickle
import numpy as np

def discover(request):
    if request.session['email']:
        email = request.session['email']
        user = registration.objects.filter(email=email)
        id = registration.objects.get(email=email)
        interests_all=interest.objects.all()
        interests=[]
        for i in interests_all:
            interests.append(i)
        userid = id.pk
        other = None
        my_id = None
        counts = 0
        count_following=0
        list_of_id = suggest_people(request)
        try:
            em = followers.objects.get(user_id=userid)
            other = [user_id for user_id in em.following.all()]
            count_following =len(other)
            my_id = [user_id for user_id in em.follow_me.all()]
            counts = len(my_id)


        except:
            pass
        user_data = userdetails.objects.all()
        mydetials = 0
        try:
            mydetials = userdetails.objects.get(owner_id=userid)
        except:
            pass
        other_user = registration.objects.all().exclude(email=email)
        trending_hashtags,res_dct=get_hash_tags()
        dict1 = {
            'email': email,
            'user': user,
            'others': other,
            'other': other_user,
            'followers': my_id,
            'count':counts,
            'count_following':count_following,
            'mydetials': mydetials,
            'userdata': user_data,
            'interests': interests,
            'trending_hashtags':trending_hashtags,
            'res_dct':res_dct,
            'list_of_id': list_of_id }

        return render(request, 'discover.html', dict1)


def newsfeed(request):
    email = request.session['email']
    try:
        profile= request.FILES['image']
    except:
        profile =None
    bio=request.POST['bio']
    inte = request.POST.getlist('interest')

    usr_id = registration.objects.get(email=email)
    usrs_id = usr_id.id

    try:
        posts = []
        try:
            p_post = userpost.objects.all()
            posts.append(p_post)
        except:
            pass

        if len(posts) > 0:
            qs = sorted(chain(*posts), reverse=True, key=lambda obj: obj.created)
    except:
        pass

    userdata = userdetails(profile_pic= profile, user_bio= bio, user_interest= inte , owner_id=usrs_id)
    userdata.save()

    return redirect('home')


def discover_more(request):
    email = request.session['email']
    f = registration.objects.get(email=email)
    # try:
    #     my_profile = followers.objects.get(user_id=f.id)
    #
    # except:
    #     my_profile = followers(user_id=f.id)
    #     my_profile.save()

    my_profile = followers.objects.get(user_id=f.id)
    pk = request.POST["follow_pk"]

    obj = registration.objects.get(id = pk)
    fol = registration.objects.get(pk=f.id)

    follow = followers.objects.get(user_id = obj.pk)


    if obj in my_profile.following.all():

        my_profile.following.remove(obj)
        follow.follow_me.remove(fol)
        # value = False
    else:

        my_profile.following.add(obj)
        follow.follow_me.add(fol)
        # value = True

    return redirect(request.META.get('HTTP_REFERER'))


def follower(request):
    if request.session['email']:
        email = request.session['email']
        user = registration.objects.filter(email=email)
        id = registration.objects.get(email=email)
        userid = id.pk
        other = None
        my_id = None
        counts =0
        count_following=0
        try:
            em = followers.objects.get(user_id=userid)
            other = [user_id for user_id in em.following.all()]
            count_following=len(other)
            my_id = [user_id for user_id in em.follow_me.all()]
            counts =len(my_id)


        except:
            pass

        user_data = userdetails.objects.all()
        mydetials = 0
        try:
            mydetials = userdetails.objects.get(owner_id=userid)
        except:
            pass
        other_user = registration.objects.all().exclude(email=email)
        trending_hashtags,res_dct=get_hash_tags()
        list_of_id = suggest_people(request)
        dict1 = {
            'email': email,
            'user': user,
            'others': other,
            'other': other_user,
            'followers': my_id,
            'count':counts,
            'count_following':count_following,
            'mydetials': mydetials,
            'userdata': user_data,
            'trending_hashtags':trending_hashtags,
            'res_dct':res_dct,
            'list_of_id': list_of_id  }

        return render(request, 'follower.html', dict1)

def following(request):
    if request.session['email']:
        email = request.session['email']
        user = registration.objects.filter(email=email)
        id = registration.objects.get(email=email)
        userid = id.pk
        other = None
        my_id = None
        counts =0
        count_following=0
        try:
            em = followers.objects.get(user_id=userid)
            other = [user_id for user_id in em.following.all()]
            count_following=len(other)
            my_id = [user_id for user_id in em.follow_me.all()]
            counts =len(my_id)


        except:
            pass

        user_data = userdetails.objects.all()
        mydetials = 0
        try:
            mydetials = userdetails.objects.get(owner_id=userid)
        except:
            pass
        other_user = registration.objects.all().exclude(email=email)
        trending_hashtags,res_dct=get_hash_tags()
        list_of_id = suggest_people(request)
        dict1 = {
            'email': email,
            'user': user,
            'others': other,
            'other': other_user,
            'followers': my_id,
            'count':counts,
            'count_following':count_following,
            'mydetials': mydetials,
            'userdata': user_data,
            'trending_hashtags':trending_hashtags,
            'res_dct':res_dct, 
            'list_of_id': list_of_id }

        return render(request, 'following.html', dict1)

def get_location(request):
    email = request.session['email']

    lng=float(request.POST.get('lng'))
    lat=float(request.POST.get('lat'))
    # print(lng)
    # print(lat)
    url='https://api.mapbox.com/geocoding/v5/mapbox.places/'+str(lng)+','+str(lat)+'.json?sypes=address&access_token=pk.eyJ1Ijoic2FtaXI4NDc1MyIsImEiOiJja29mbTFiMGMwbm10MnVyMGs2MGJwM2FyIn0.AVzoRvG6EmclKtdIsSeRkw'
    address=requests.get(url).json()

    locality=address['features'][0]['context'][0]['text']
    place=address['features'][0]['context'][1]['text']
    district=address['features'][0]['context'][2]['text']
    region=address['features'][0]['context'][3]['text']
    country=address['features'][0]['context'][4]['text']
   
    address=locality+','+district+','+country

    user=registration.objects.get(email=email)
    user_id=user.id

    if user_location_data.objects.filter(user_id=user_id).exists()==False:
        user_location=user_location_data(user_id=user_id,latitude=lat,longitude=lng,address=address)
        user_location.save()
    else:
        user_location=user_location_data.objects.get(user_id=user.id)
        user_location.latitude=lat
        user_location.longitude=lng
        user_location.address=address
        user_location.save(update_fields=['latitude','longitude','address'])
        
    
       
    return render(request, 'index.html')

import geopy.distance as geodist
def calc_distance(cor1,cor2):
    distance=geodist.geodesic(cor1, cor2).km
    return distance

def get_search(request):
    email = request.session['email']
    uid = registration.objects.get(email=email)
    user_id=uid.id
    

    u_interest=request.POST.get('interest')
    distance=request.POST.get('distance')

    #get user lon,lat
    user_location=user_location_data.objects.get(user_id=uid.id)
    user_cord=(user_location.latitude,user_location.longitude)
   
    users=userdetails.objects.all().exclude(owner_id=user_id)
    user_match=[]
    for i in users:
        lis=i.user_interest
        if lis.find(u_interest) != -1:
            user_match.append(i.owner_id)
        else:
            pass

    matched_user_id=[]
    matched_user_coordinate=[]
    for i in user_match:
        friend=user_location_data.objects.get(user_id=i)
        coordinate=(friend.latitude,friend.longitude)
       
        friend_distance=calc_distance(user_cord,coordinate)
        
        if float(friend_distance)<=float(distance):
            matched_user_coordinate.append(coordinate)
            matched_user_id.append(i)

    json_coor=json.dumps(matched_user_coordinate)

    u_data=[]
    for i in matched_user_id:
        userdata=registration.objects.filter(id=i)
        u_data.append(userdata)
    

    user = registration.objects.filter(email=email)
    id = registration.objects.get(email=email)
    interests_all=interest.objects.all()
    interests=[]
    for i in interests_all:
        interests.append(i)
    userid = id.pk
    other = None
    my_id = None
    counts = 0
    count_following=0
    try:
        em = followers.objects.get(user_id=userid)
        other = [user_id for user_id in em.following.all()]
        count_following =len(other)
        my_id = [user_id for user_id in em.follow_me.all()]
        counts = len(my_id)


    except:
        pass
    user_data = userdetails.objects.all()
    mydetials = 0
    try:
        mydetials = userdetails.objects.get(owner_id=userid)
    except:
        pass
    other_user = registration.objects.all().exclude(email=email)
    trending_hashtags,res_dct=get_hash_tags()
    list_of_id = suggest_people(request)
    dict1 = {
        'email': email,
        'user': user,
        'others': other,
        'other': other_user,
        'followers': my_id,
        'count':counts,
        'count_following':count_following,
        'mydetials': mydetials,
        'userdata': user_data,
        'interests': interests,
        'u_data':u_data,
        'json_coor':json_coor,
        'trending_hashtags':trending_hashtags,
        'res_dct':res_dct, 
        'list_of_id': list_of_id }
   

    return render(request, 'discover.html', dict1)



# ----------------------------------------------------------------------------------------------
# AI part
import random
def suggest_people(request):
    if request.session['email']:
        email = request.session['email']
        id = registration.objects.get(email=email)
        userid = id.pk

        conn = psycopg2.connect(host="localhost",database='spotster', user = "postgres", password = "postgres@123")
        query1 = 'SELECT * FROM "complete_userdetails"'
        conn.autocommit = True
        dataset1 = sqlio.read_sql_query(query1,conn)

        conn = psycopg2.connect(host="localhost",database='spotster', user = "postgres", password = "postgres@123")
        query2 = 'SELECT * FROM "discover_interest"'
        conn.autocommit = True
        dataset2 = sqlio.read_sql_query(query2,conn)

        conn = psycopg2.connect(host="localhost",database='spotster', user = "postgres", password = "postgres@123")
        query3 = 'SELECT * FROM "discover_followers_follow_me"'
        conn.autocommit = True
        dataset3 = sqlio.read_sql_query(query3,conn)

        dataset = pd.DataFrame(columns=['owner_id', 'Interests_id', 'following_to'])
        features = ['Interests_id', 'following_to']
        # label = ['owner_id']

        values = []
        key = []
        follow = []
        for i in range(0,len(dataset1)):
            list_interest = []
            x = dataset1['user_interest'][i]
            x = x.replace("'","")
            x = x.strip('][').split(', ')
            # print(x)
            for j in x:
                d2 = dataset2.loc[dataset2['my_interest']==j]
                for k in d2['id']:
                    unique_id = dataset3['registration_id'].unique()
                    for ident in unique_id:
                        d3 = dataset3.loc[dataset3['registration_id']==ident]
                        d1 = []
                        for d in d3['followers_id']:
                            d1.append(d)
                            if ident==dataset1['owner_id'][i]:
                                for dz in d1:
                                    values.append(k)
                                    key.append(dataset1['owner_id'][i])
                                    follow.append(dz)
        dataset['owner_id'] = key
        dataset['Interests_id'] = values
        dataset['following_to'] =follow
        try:
            test = dataset.loc[dataset['owner_id']==userid]
            test = test[features]

            loaded_model = pickle.load(open('discover/RandomForest', 'rb'))
            predicted_id_rfc = loaded_model.predict(test)
            bbb = list(np.unique(predicted_id_rfc))
            b0 = list(np.unique(test['following_to']))
            suggest_list = []
            for num_id in bbb:
                if num_id in b0:
                    pass
                else:
                    suggest_list.append(num_id)
            if userid in suggest_list:
                suggest_list.remove(userid)
            if len(suggest_list)>5:
                list_of_names = random.sample(suggest_list,5)
            else:
                list_of_names = suggest_list  
            tar = []
            for items in list_of_names:
                var = registration.objects.get(id=items)
                tar.append(var)
            return tar
        except:
            return None    
