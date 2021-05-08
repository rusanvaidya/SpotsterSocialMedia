from django.shortcuts import render
from home.models import registration,userpost
from complete.models import userdetails
from discover.models import followers,interest
from itertools import chain
# Create your views here.

def profile(request):
    if request.session['email']:
        email = request.session['email']
        usr_id = registration.objects.get(email=email)
        usrs_id = usr_id.id


        try:
            update_id = userdetails.objects.get(owner_id = usrs_id)

        except:
            profile1 = None
            bio = ''
            inte = ''
            userdata = userdetails(profile_pic= profile1, user_bio= bio, user_interest= inte , owner_id=usrs_id)
            userdata.save()


        try:
            update_profile  = request.FILES['image']
            some = userdetails.objects.get(owner_id=usrs_id)
            bio =some.user_bio
            interest1 = some.user_interest
            userdetails.objects.filter(owner_id=usrs_id).delete()
            my = userdetails(profile_pic= update_profile, user_bio= bio, user_interest= interest1 , owner_id=usrs_id)
            my.save()


        except:
            pass

        user = registration.objects.filter(email=email)

        other = None
        my_id = None
        counts = 0
        count_following = 0
        try:
            em = followers.objects.get(user_id=usrs_id)
            other = [user_id for user_id in em.following.all()]
            count_following = len(other)
            my_id = [user_id for user_id in em.follow_me.all()]
            counts = len(my_id)



        except:

            pass

        # try:
        #     mydetials = userdetails.objects.get(owner_id= usrs_id)
        #
        # except:
        #     pass
        posts =[]
        qs=None
        pu = registration.objects.all()
        my_post = userpost.objects.filter(author_id=usrs_id)
        posts.append(my_post)
        if len(posts) > 0:
            qs = sorted(chain(*posts), reverse=True, key=lambda obj: obj.created)

        interest_list = interest.objects.all()
        mydetials = userdetails.objects.get(owner_id=usrs_id)
        user_data = userdetails.objects.all()
        dict1 = {
            'email': email,
            'user': user,
            'others': other,
            'followers': my_id,
            'count': counts,
            'count_following': count_following,
            'interest': interest_list,
            'posts':qs,
            'pu':pu,
            'mydetials':mydetials,
            'userdata':user_data}
        return render(request, 'profile.html',dict1)