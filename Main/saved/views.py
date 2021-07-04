from django.shortcuts import render, redirect
from home.models import registration
# Create your views here.
from discover.models import followers

from complete.models import userdetails


def saved(request):
    if request.session['email']:
        email = request.session['email']
        user = registration.objects.filter(email=email)
        id = registration.objects.get(email=email)
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
        dict1 = {
            'email': email,
            'user': user,
            'others': other,
            'other': other_user,
            'followers': my_id,
            'count': counts,
            'count_following': count_following,
            'mydetials': mydetials,
            'userdata': user_data}

        return render(request, 'saved.html', dict1)

def saved_post(request):
    return redirect(request.META.get('HTTP_REFERER'))