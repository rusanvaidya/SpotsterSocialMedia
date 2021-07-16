from django.shortcuts import render, redirect
from home.models import registration,userpost,Like,comment
from complete.models import userdetails
from discover.models import followers,interest
from itertools import chain
from django.contrib import messages
from trending.views import get_hash_tags
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
            # bio =some.user_bio
            # interest1 = some.user_interest
            # userdetails.objects.filter(owner_id=usrs_id).delete()
            some.profile_pic= update_profile
            some.save()


        except:
            pass

        user = registration.objects.filter(email=email)

        other = None
        my_id = None
        counts = 0
        count_following = 0
        my_post_count = 0
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
        my_post_count = my_post.count()
        if len(posts) > 0:
            qs = sorted(chain(*posts), reverse=True, key=lambda obj: obj.created)

        interest_list = interest.objects.all().order_by('my_interest')
        mydetials = userdetails.objects.get(owner_id=usrs_id)
        user_data = userdetails.objects.all()

        like_unlike = None
        try:
            like_unlike = Like.objects.all()


        except:
            pass
        comments = None
        try:
            comments = comment.objects.all()
        except:
            pass
        trending_hashtags=get_hash_tags()
        dict1 = {
            'email': email,
            'user': user,
            'others': other,
            'followers': my_id,
            'count': counts,
            'my_post_count': my_post_count,
            'count_following': count_following,
            'interest': interest_list,
            'posts':qs,
            'pu':pu,
            'mydetials':mydetials,
            'like_unlike': like_unlike,
            'userdata':user_data,
            'comments':comments,
            'trending_hashtags':trending_hashtags}
        return render(request, 'profile.html',dict1)

    return render(request,'index.html')


def profile_update(request):
    if request.session['email']:
        email = request.session['email']
        usr_id = registration.objects.get(email=email)
        usrs_id = usr_id.id

        user = registration.objects.filter(email=email)

        other = None
        my_id = None
        counts = 0
        count_following = 0
        my_post_count = 0
        try:
            em = followers.objects.get(user_id=usrs_id)
            other = [user_id for user_id in em.following.all()]
            count_following = len(other)
            my_id = [user_id for user_id in em.follow_me.all()]
            counts = len(my_id)



        except:

            pass

        posts =[]
        qs=None
        pu = registration.objects.all()
        my_post = userpost.objects.filter(author_id=usrs_id)
        posts.append(my_post)
        my_post_count = my_post.count()
        if len(posts) > 0:
            qs = sorted(chain(*posts), reverse=True, key=lambda obj: obj.created)

        interest_list = interest.objects.all().order_by('my_interest')
        mydetials = userdetails.objects.get(owner_id=usrs_id)
        user_data = userdetails.objects.all()

        like_unlike = None
        try:
            like_unlike = Like.objects.all()


        except:
            pass

        comments = None
        try:
            comments = comment.objects.all()
        except:
            pass
        dict1 = {
            'email': email,
            'user': user,
            'others': other,
            'followers': my_id,
            'count': counts,
            'my_post_count': my_post_count,
            'count_following': count_following,
            'interest': interest_list,
            'posts': qs,
            'pu': pu,
            'mydetials': mydetials,
            'like_unlike': like_unlike,
            'userdata': user_data,
            'comments':comments}

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        change_email = request.POST['email']
        change_bio = request.POST['bio']
        current_pass = request.POST['current_pass']
        new_pass = request.POST['new_pass']
        re_new_pass = request.POST['re_new_pass']

        if current_pass == '':
            messages.info(request, 'Required current password to save Changes !!!')
            return render(request, "profile.html", dict1)


        elif current_pass != usr_id.password:
            messages.info(request,'Password Incorrect!!!')
            return render(request, "profile.html", dict1)

        elif current_pass == usr_id.password:
            if usr_id.first_name == first_name and usr_id.last_name == last_name and usr_id.email == change_email and mydetials.user_bio == change_bio:
                if new_pass == '' and re_new_pass == '':
                    messages.info(request, 'No changes are Detected!!!')
                    return render(request, "profile.html", dict1)


            else:
                if usr_id.email != change_email:
                    usr_id.first_name = first_name
                    usr_id.last_name = last_name
                    usr_id.email = change_email
                    mydetials.user_bio = change_bio
                    if new_pass != '' and re_new_pass != '' and new_pass == re_new_pass:
                        usr_id.password = new_pass
                    usr_id.save()
                    mydetials.save()
                    messages.info(request, 'Email is Changed Login please!!!')
                    del request.session['email']
                    return render(request, 'index.html')
                usr_id.first_name = first_name
                usr_id.last_name = last_name
                usr_id.email = change_email
                mydetials.user_bio = change_bio

                if new_pass != '' and re_new_pass != '' and new_pass == re_new_pass:
                    usr_id.password = new_pass

                usr_id.save()
                mydetials.save()
                messages.info(request, 'Data Saved!!!')
                return render(request, "profile.html", dict1)

        if new_pass != '' and re_new_pass != '' and new_pass == re_new_pass:
            usr_id.password = new_pass
            usr_id.save()
            messages.info(request, 'Password Changed!!!')
            return render(request,"profile.html",dict1)

        if new_pass != '' and re_new_pass != '' and new_pass != re_new_pass:
            messages.info(request, 'New password and Confirm Password do not match!!!')
            return render(request, "profile.html", dict1)

        return render(request,"profile.html",dict1)
    return render(request, 'index.html')

def interest_update(request):
    if request.session['email']:
        email = request.session['email']
        usr_id = registration.objects.get(email=email)
        usrs_id = usr_id.id

        user = registration.objects.filter(email=email)

        other = None
        my_id = None
        counts = 0
        count_following = 0
        my_post_count = 0
        try:
            em = followers.objects.get(user_id=usrs_id)
            other = [user_id for user_id in em.following.all()]
            count_following = len(other)
            my_id = [user_id for user_id in em.follow_me.all()]
            counts = len(my_id)



        except:

            pass

        posts = []
        qs = None
        pu = registration.objects.all()
        my_post = userpost.objects.filter(author_id=usrs_id)
        posts.append(my_post)
        my_post_count = my_post.count()
        if len(posts) > 0:
            qs = sorted(chain(*posts), reverse=True, key=lambda obj: obj.created)

        interest_list = interest.objects.all().order_by('my_interest')
        mydetials = userdetails.objects.get(owner_id=usrs_id)
        user_data = userdetails.objects.all()

        like_unlike = None
        try:
            like_unlike = Like.objects.all()


        except:
            pass

        comments = None
        try:
            comments = comment.objects.all()
        except:
            pass

        inte = request.POST.getlist('interest')
        if inte:
            interestupdate = userdetails.objects.get(owner_id = usr_id)
            interestupdate.user_interest = inte
            interestupdate.save()
            mydetials = userdetails.objects.get(owner_id = usrs_id)
            messages.info(request, 'Change is made!!!')


        else:
            messages.info(request, 'Nothing Selected!!!')

        dict1 = {
            'email': email,
            'user': user,
            'others': other,
            'followers': my_id,
            'count': counts,
            'my_post_count': my_post_count,
            'count_following': count_following,
            'interest': interest_list,
            'posts': qs,
            'pu': pu,
            'mydetials': mydetials,
            'like_unlike': like_unlike,
            'userdata': user_data,
            'comments':comments}
        return render(request, "profile.html",dict1)

def view_profile(request):
    if request.session['email']:
        email = request.session['email']
        usrid = request.GET.get('id')

        usr_id = registration.objects.get(email=email)
        usrs_id = usr_id.id


        user = registration.objects.filter(email=email)
        userview = registration.objects.filter(id=usrid)

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
        posts = []
        qs = None
        pu = registration.objects.all()
        my_post = userpost.objects.filter(author_id=usrid)
        posts.append(my_post)
        vmy_post_count = my_post.count()
        if len(posts) > 0:
            qs = sorted(chain(*posts), reverse=True, key=lambda obj: obj.created)

        interest_list = interest.objects.all().order_by('my_interest')
        mydetials = userdetails.objects.get(owner_id=usrs_id)
        udetials = userdetails.objects.get(owner_id=usrid)
        user_data = userdetails.objects.all()

        like_unlike = None
        comments=None
        try:
            like_unlike = Like.objects.all()


        except:
            pass

        comments = None
        try:
            comments = comment.objects.all()
        except:
            pass

        vcounts = 0
        vcount_following = 0
        try:
            em = followers.objects.get(user_id=usrid)
            vother = [user_id for user_id in em.following.all()]
            vcount_following = len(vother)
            vmy_id = [user_id for user_id in em.follow_me.all()]
            vcounts = len(vmy_id)



        except:

            pass
        try:
            comments=comment.objects.all()
        except:
            pass
        dict1 = {
            'email': email,
            'user': user,
            'userview': userview,
            'others': other,
            'followers': my_id,
            'count': counts,
            'vcount': vcounts,
            'my_post_count': vmy_post_count,
            'count_following': count_following,
            'vcount_following': vcount_following,
            'interest': interest_list,
            'posts': qs,
            'pu': pu,
            'mydetials': mydetials,
            'udetials': udetials,
            'like_unlike': like_unlike,
            'userdata': user_data,
            'comments':comments}
        if int(usrid) == usrs_id:
            return redirect('profile')
        else:
            return render(request, 'user_profile_viewer.html', dict1)

    return render(request, 'index.html')
