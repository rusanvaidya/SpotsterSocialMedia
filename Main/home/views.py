from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from discover.models import followers

from discover.models import interest,user_coordinate

from complete.models import userdetails
from .models import registration, support, userpost, Like, comment
from django.contrib import messages
from itertools import chain
from math import sin, cos, sqrt, atan2, radians
# Create your views here.
def home(request):
    try:
        if request.session['email']:
            email = request.session['email']
            user = registration.objects.filter(email=email)
            usr_id = registration.objects.get(email=email)
            usrs_id = usr_id.id
            other = None
            my_id = None
            counts = 0
            my_post_count = 0
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
                my_post_count = my_post.count()
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
                'count':counts,
                'my_post_count':my_post_count,
                'count_following':count_following,
                'interest':interest_list,
                'posts':qs,
                'pu':pu,
                'mydetials':mydetials,
                'userdata':user_data,
                'like_unlike':like_unlike,
                'comments':comments}
                # 'country': country,
                # 'city': city}

            if 'term' in request.GET:

                qs = interest.objects.filter(my_interest__startswith=request.GET.get('term'))
                titles = list()
                for product in qs:
                    titles.append(product.my_interest)
                return JsonResponse(titles, safe=False)
            return render(request, 'newsfeed.html', dict1)
        else:
            return render(request, 'index.html')


    except:
        return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = registration.objects.filter(email=email, password=password)
        if user.exists():
            request.session['email'] = email
            return redirect('home')
        else:
            messages.info(request, 'Incorrect Email or Password!!!')
            return render(request, 'index.html')

    else:
        messages.info(request, 'Page not found!!!')
        return render(request,'index.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']
        birth_month = request.POST['birth_month']
        birth_day = request.POST['birth_day']
        birth_year = request.POST['birth_year']
        gender = request.POST.get('sex')

        # password = base64.encodebytes(password)
        birthday = birth_day + '-' + birth_month + '-' + birth_year

        if registration.objects.filter(email=email).exists():
            messages.info(request, 'This Email is already Taken')
            return render(request, 'index.html')

        elif password != repassword:
            messages.info(request, 'Password donot match!!!')
            return render(request,'index.html')

        else:
            user = registration(first_name=first_name, last_name=last_name, email=email, password=password,
                                birthday=birthday, gender=gender)
            user.save()
            user = registration.objects.filter(email=email, password=password)
            if user.exists():
                request.session['email'] = email
                usr_id = registration.objects.get(email=email)
                usrs_id = usr_id.id
                interest_list = interest.objects.all().order_by('my_interest')
                other = None
                try:
                    em = followers.objects.get(user_id=usrs_id)
                    other = [user_id for user_id in em.following.all()]

                except:
                    pass
                # other_user = registration.objects.all().exclude(email=email)

                f = registration.objects.get(email=email)
                try:
                    followers.objects.get(user_id=f.id)

                except:
                    my_profile = followers(user_id=f.id)
                    my_profile.save()
                return render(request, 'complete.html', {'email': email, 'user': user, 'others': other,'interest':interest_list})
            else:
                messages.info(request, 'User not exits!!!')
                return render(request, 'index.html')
    else:

        messages.info(request, 'Page not found!!!')
        return render(request, 'index.html', {'email': None, 'user': None})


def logout(request):

    try:
        if request.method == 'GET':
            del request.session['email']
            return render(request, 'index.html')
    except KeyError:
        return render(request, 'index.html')


def support_view(request):
    return render(request,'support.html')

def support_action(request):
    u_name=request.POST.get('uname')
    u_email=request.POST.get('uemail')
    u_message=request.POST.get('umessage')

    support_save=support(name=u_name,email=u_email,message=u_message)
    support_save.save()
    return redirect('supportpage')

def get_location(request):
    email = request.session['email']

    lng=float(request.POST.get('lng'))
    lat=float(request.POST.get('lat'))
    
    user=registration.objects.get(email=email)
    user_id=user.id

    if user_coordinates.objects.filter(user_id=user_id).exists()==False:
        user_location=user_coordinates(user_id=user_id,latitude=lat,longitude=lng)
        user_location.save()
    else:
        user_location=user_coordinates.objects.get(user_id=user.id)
        user_location.latitude=lat
        user_location.longitude=lng
        user_location.save(update_fields=['latitude','longitude'])
        
    
       
    return render(request, 'index.html')

# import geopy.distance as geodist
# def calc_distance(cor1,cor2):
#     distance=geodist.geodesic(cor1, cor2).km
#     print(distance)
def user_post(request):
    email = request.session['email']
    user_feeling = request.POST['feeling']
    user_emoji = request.POST['emoji']
    user_content = request.POST['content']
    try:
        user_files = request.FILES['ufiles']
    except:
        user_files =None
    if user_feeling == '' and user_emoji == '' and user_files == None and user_content == '':
        return redirect('home')
    usr_id = registration.objects.get(email=email)
    usrs_id = usr_id.id

    user_data = userpost(feeling=user_feeling,emoji=user_emoji,usercontent=user_content,userfile=user_files,author_id=usrs_id)
    user_data.save()
    return redirect('home')

def notification(request):
    if request.session['email']:
        email = request.session['email']
        user = registration.objects.filter(email=email)
    dict1 = {
        'email': email,
        'user': user,
    }
    return render(request, 'notification.html', dict1)

def post_comment(request):
    if request.session['email']:
        email = request.session['email']
        user = registration.objects.filter(email=email)
        usr_id = registration.objects.get(email=email)
        usrs_id = usr_id.id
        other = None
        my_id = None
        counts = 0
        my_post_count = 0
        count_following = 0
        pu = registration.objects.all()
        qs = None

        try:
            em = followers.objects.get(user_id=usrs_id)
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

            my_post = userpost.objects.filter(author_id=profile1.id)
            my_post_count = my_post.count()
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

        like_unlike = None
        try:
            like_unlike = Like.objects.all()

        except:
            pass


        postid = int(request.GET['pid'])


        comm = comment.objects.filter(post_id = postid).order_by('created_date')
        comm_count = comment.objects.filter(post_id = postid).count()

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
            'userdata': user_data,
            'like_unlike': like_unlike,
            'postid':postid,
            'comment':comm,
            'comment_count':comm_count}
        # 'country': country,
        # 'city': city}

        if 'term' in request.GET:

            qs = interest.objects.filter(my_interest__startswith=request.GET.get('term'))
            titles = list()
            for product in qs:
                titles.append(product.my_interest)
            return JsonResponse(titles, safe=False)
        return render(request, 'post.html', dict1)
    else:
        return render(request, 'index.html')


def like_post(request):
    if request.method == 'POST':
        email = request.session['email']
        post_id = request.POST.get('postid')
        post_obj = userpost.objects.get(pk = post_id)
        author_id = post_obj.author_id


        profile = registration.objects.get(email=email)




        if profile in post_obj.liked.all():
            post_obj.liked.remove(profile)
        else:
            post_obj.liked.add(profile)

        like, created = Like.objects.get_or_create(user_id=profile.pk, post_id=post_id)
        like.save()

        if not created:
            if like.value =='Like':
                like.value='Unlike'
                # pri = Like.objects.get(user_id=profile.pk, post_id=post_id)
                # Like.objects.filter(id=pri.id).delete()

            else:

                like.value ='Like'
        else:

            like.value='Like'

        post_obj.save()
        like.save()
    return redirect(request.META.get('HTTP_REFERER'))


def comment_post(request):
    if request.session['email']:
        email = request.session['email']
        user = registration.objects.filter(email=email)
        usr_id = registration.objects.get(email=email)
        usrs_id = usr_id.id
        other = None
        my_id = None
        counts = 0
        my_post_count = 0
        count_following = 0
        pu = registration.objects.all()
        qs = None

        try:
            em = followers.objects.get(user_id=usrs_id)
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

            my_post = userpost.objects.filter(author_id=profile1.id)
            my_post_count = my_post.count()
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

        like_unlike = None
        try:
            like_unlike = Like.objects.all()

        except:
            pass

        userid = request.POST['userid']
        postid = request.POST['postid']
        comment_message = request.POST['comment']

        if comment_message == '':
            pass

        else:
            comm, created = comment.objects.get_or_create(user_id=userid, post_id=postid, comments=comment_message)
            comm.save()


        comm = comment.objects.filter(post_id=postid).order_by('created_date')
        comm_count = comment.objects.filter(post_id=postid).count()

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
            'userdata': user_data,
            'like_unlike': like_unlike,
            'postid': int(postid),
            'comment': comm,
            'comment_count': comm_count}
        # 'country': country,
        # 'city': city}

        return render(request, 'post.html', dict1)
    else:
        return render(request, 'index.html')
