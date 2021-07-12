from itertools import chain

from django.shortcuts import render, redirect
from home.models import registration
# Create your views here.
from discover.models import followers,interest
from complete.models import userdetails

from home.models import userpost


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
            'interests': interests }

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
        dict1 = {
            'email': email,
            'user': user,
            'others': other,
            'other': other_user,
            'followers': my_id,
            'count':counts,
            'count_following':count_following,
            'mydetials': mydetials,
            'userdata': user_data }

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
        dict1 = {
            'email': email,
            'user': user,
            'others': other,
            'other': other_user,
            'followers': my_id,
            'count':counts,
            'count_following':count_following,
            'mydetials': mydetials,
            'userdata': user_data }

        return render(request, 'following.html', dict1)

def get_search(request):
    interest=request.POST.get('interest')
    distance=request.POST.get('distance')
    print(interest)
    print(distance)
    return render(request, 'index.html')