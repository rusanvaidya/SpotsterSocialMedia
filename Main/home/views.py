from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from discover.models import followers

from discover.models import interest

from complete.models import userdetails
from .models import registration, support, userpost
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
                'userdata':user_data}
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
            usr_id = registration.objects.get(email=email)
            usrs_id = usr_id.id
            other = None
            my_id = None
            counts=0
            count_following =0
            pu = registration.objects.all()
            qs = None
            try:
                em = followers.objects.get(user_id = usrs_id)
                other = [user_id for user_id in em.following.all()]
                count_following=len(other)
                my_id = [user_id for user_id in em.follow_me.all()]
                counts=len(my_id)



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
                posts.append(my_post)
                if len(posts) > 0:
                    qs = sorted(chain(*posts), reverse=True, key=lambda obj: obj.created)
            except:
                pass

            user_data = userdetails.objects.all()
            mydetials = 0
            try:
                mydetials = userdetails.objects.get(owner_id=usrs_id)
            except:
                pass

            dict1 = {
            'email': email,
            'user': user,
            'others': other,
            'followers':my_id,
            'count':counts,
            'count_following':count_following,
            'pu':pu,
            'posts':qs,
            'mydetials':mydetials,
            'userdata':user_data}
            return render(request, 'newsfeed.html', dict1)
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
                interest_list = interest.objects.all()
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
    lng=float(request.POST.get('lng'))
    lat=float(request.POST.get('lat'))
    print(lng)
    print(lat)
    return render(request, 'index.html')

# import geopy.distance as geodist
# def calc_distance(cor1,cor2):
#     distance=geodist.geodesic(cor1, cor2).km
#     print(distance)
def user_post(request):
    email = request.session['email']
    user_feeling = request.POST['feeling']
    user_emoji = request.POST['emoji']
    print(user_emoji)
    user_content = request.POST['content']
    try:
        user_files = request.FILES['ufiles']
    except:
        user_files =None
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

def post(request):
    if request.session['email']:
        email = request.session['email']
        user = registration.objects.filter(email=email)
    dict1 = {
        'email': email,
        'user': user,
    }
    return render(request, 'post.html', dict1)
