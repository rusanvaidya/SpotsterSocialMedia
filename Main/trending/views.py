from itertools import chain

from django.shortcuts import render
from home.models import registration,userpost
from discover.models import followers

from home.models import userpost,Like,comment

from complete.models import userdetails
from discover.models import interest

import re

def trending(request):
    try:
        if request.session['email']:
            email = request.session['email']
            user = registration.objects.filter(email=email)
            usr_id = registration.objects.get(email=email)
            usrs_id = usr_id.id
            other = None
            my_id = None
            counts = 0
            count_following =0
            pu = registration.objects.all()
            qs = None

            try:
                em = followers.objects.get(user_id=usrs_id)
                other = [user_id for user_id in em.following.all()]
                count_following= len(other)
                my_id = [user_id for user_id in em.follow_me.all()]
                counts = len(my_id)



            except:

                pass


            try:
                profile1 = registration.objects.get(email=email)
                profile = followers.objects.get(user_id=profile1.pk)
                users1 = [i for i in profile.following.all()]
                posts =[]
                for u in users1:
                    p = registration.objects.get(id=u.id)
                    try:
                        p_post = userpost.objects.filter(author_id=p.id)
                        posts.append(p_post)
                    except:
                        pass

                my_post = userpost.objects.filter(author_id=profile1.id)
                posts.append(my_post)
                if len(posts) > 0:
                    qs = sorted(chain(*posts), reverse=True, key=lambda obj: obj.created)
            except:
                pass
            interest_list = interest.objects.all()
            user_data = userdetails.objects.all()
            mydetials = 0
            try:
                mydetials = userdetails.objects.get(owner_id=usrs_id)
            except:
                pass
            posts=userpost.objects.all()
            
            my_post = userpost.objects.all()
            trendingpost = []
            for ids in my_post:
                if ids.liked.all().count() > 1:
                    nu = ids.id
                    dat = userpost.objects.filter(id=nu)
                    trendingpost.append(dat)

            trend = sorted(chain(*trendingpost), reverse=True, key=lambda obj: obj.created)

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
            trending_hashtags,res_dct=get_hash_tags()
            hashtag=request.GET.get('topic')
            if hashtag!=None:
                hashtag='#'+hashtag
                trend=userpost.objects.filter(usercontent__iregex=hashtag)

            dict1 = {
                'email': email,
                'user': user,
                'others': other,
                'followers': my_id,
                'count':counts,
                'count_following':count_following,
                'interest':interest_list,
                'posts':qs,
                'pu':pu,
                'mydetials':mydetials,
                'userdata':user_data,
                'trend':trend,
                'like_unlike':like_unlike,
                'comments':comments,
                'trending_hashtags':trending_hashtags,
                'res_dct':res_dct
                }


            return render(request, 'trending.html', dict1)
        else:
            return render(request, 'index.html')


    except:
        return render(request, 'index.html')

def get_hash_tags():
    from datetime import datetime, timedelta
    posts=userpost.objects.filter()
    post_likes=[]
    usertext=[]
    for i in posts:
        usertext.append(i.usercontent)
    pattern='#\w+'
    hashtags=[re.findall(pattern,i) for i in usertext]
    hashtags=sum(hashtags,[])

    delta = []
    for x in hashtags:
        if x not in delta:
            delta.append(x)

    for i in delta:
        h=[]
        post_withhash=userpost.objects.filter(usercontent__iregex=i)
        post_likes.append(i[1:])
        for a in post_withhash:
            h.append(a.num_likes)

        post_likes.append(sum(h))
    res_dct = {post_likes[i]: post_likes[i + 1] for i in range(0, len(post_likes), 2)}

    hashtags = [e[1:] for e in hashtags]
    count={i:hashtags.count(i) for i in hashtags}
    hash_dict =sorted(count.items(), key=lambda x: x[1],reverse=True)[:5]

    return dict(hash_dict),res_dct


    




