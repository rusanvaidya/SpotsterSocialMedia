from itertools import chain

from django.contrib import messages
from django.shortcuts import render, redirect
from home.models import registration,comment,userpost,Like
# Create your views here.
from discover.models import followers

from complete.models import userdetails

from saved.models import user_saved_post,flag_inappropriate
from trending.views import get_hash_tags

def saved(request):
    if request.session['email']:
        email = request.session['email']
        user = registration.objects.filter(email=email)
        id = registration.objects.get(email=email)
        userid = id.pk
        other = None
        my_id = None
        qs = None
        counts = 0
        count_following = 0
        pu = registration.objects.all()
        try:
            em = followers.objects.get(user_id=userid)
            other = [user_id for user_id in em.following.all()]
            count_following = len(other)
            my_id = [user_id for user_id in em.follow_me.all()]
            counts = len(my_id)


        except:
            pass


        try:
            profile1 = registration.objects.get(email=email)
            profile = followers.objects.get(user_id=profile1.pk)
            users1 = [i for i in profile.following.all()]
            posts = []
            for u in users1:
                p = registration.objects.get(id=u.id)
                try:
                    p_post = userpost.objects.filter(author_id=p.id)
                    posts.append(p_post)
                except:
                    pass

            if len(posts) > 0:
                qs = sorted(chain(*posts), reverse=True, key=lambda obj: obj.created)
        except:
            pass

        user_data = userdetails.objects.all()
        mydetials = 0
        try:
            mydetials = userdetails.objects.get(owner_id=userid)
        except:
            pass

        savepost = user_saved_post.objects.filter(user_id = userid).order_by('created_date')
        other_user = registration.objects.all().exclude(email=email)
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
            'other': other_user,
            'followers': my_id,
            'count': counts,
            'posts': qs,
            'pu': pu,
            'count_following': count_following,
            'mydetials': mydetials,
            'userdata': user_data,
            'savepost':savepost,
            'like_unlike':like_unlike,
            'comments':comments,
            'trending_hashtags':trending_hashtags}

        return render(request, 'saved.html', dict1)

def saved_post(request):
    userid = request.POST['userid']
    postid = request.POST['postid']
    savepost, created = user_saved_post.objects.get_or_create(user_id=int(userid), post_id=int(postid))
    savepost.save()
    if not created:
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect(request.META.get('HTTP_REFERER'))

def remove_post(request):
    userid = request.POST['userid']
    postid = request.POST['postid']
    user_saved_post.objects.get(user_id=int(userid), post_id=int(postid)).delete()
    return redirect('saved')


def delete_post(request):
    userid = request.POST['userid']
    postid = request.POST['postid']
    userpost.objects.get(author_id=int(userid), id=int(postid)).delete()
    messages.info(request,"Your Post is Deleted!!!")
    return redirect('profile')


def edit_post(request):
    postid = request.POST['postid']
    authorid = request.POST['authorid']
    editcaption = request.POST['edit_caption']
    edit = userpost.objects.get(author_id=int(authorid), id=int(postid))
    edit.usercontent = editcaption
    edit.save()
    messages.info(request, "Your Post is edited!!!")
    return redirect('profile')




def flag_post(request):
    userid = request.POST['userid']
    postid = request.POST['postid']
    flagpost, created = flag_inappropriate.objects.get_or_create(user_id=int(userid), post_id=int(postid))
    flagpost.save()
    flags = flag_inappropriate.objects.filter(post_id = postid ).count()
    if flags == 10:
        userpost.objects.get(author_id=int(userid), id=int(postid)).delete()
        return redirect(request.META.get('HTTP_REFERER'))

    return redirect(request.META.get('HTTP_REFERER'))
