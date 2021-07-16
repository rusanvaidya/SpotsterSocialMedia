from django.shortcuts import render
from home.models import registration
# Create your views here.
from discover.models import interest,followers

from complete.models import userdetails
from trending.views import get_hash_tags

def chatbox(request):
    if request.session['email']:
        email = request.session['email']
        user = registration.objects.filter(email=email)
        id = registration.objects.get(email=email)
        interests_all = interest.objects.all()
        interests = []
        for i in interests_all:
            interests.append(i)
        userid = id.pk
        other = None
        my_id = None
        counts = 0
        count_following = 0
        try:
            em = followers.objects.get(user_id=userid)
            other = [user_id for user_id in em.following.all()]
            count_following = len(other)
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
        trending_hashtags=get_hash_tags()
        dict1 = {
            'email': email,
            'user': user,
            'others': other,
            'other': other_user,
            'followers': my_id,
            'count': counts,
            'count_following': count_following,
            'mydetials': mydetials,
            'userdata': user_data,
            'interests': interests,
            'trending_hashtags':trending_hashtags}

        return render(request, 'chatbox.html', dict1)

def room(request, room_name):
    email = request.session['email']
    user = registration.objects.filter(email=email)
    return render(request, 'chatbox.html', {
        'room_name': room_name,
        'email':email,
        'user':user})
