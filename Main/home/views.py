from django.shortcuts import render
from .models import registration, support
from django.contrib import messages
from math import sin, cos, sqrt, atan2, radians
# Create your views here.
def home(request):
    if 'email' in request.session:
        email = request.session['email']
        user = registration.objects.filter(email=email)
        other_user = registration.objects.filter().exclude(email=email)
        dict1 = {
            'email': email, 
            'user': user,
            'others': other_user}
        return render(request, 'newsfeed.html', dict1)
    else:
        return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = registration.objects.filter(email=email, password=password)
        if user.exists():
            request.session['email'] = email
            other_user = registration.objects.filter().exclude(email=email)
            dict1 = {
            'email': email, 
            'user': user,
            'others': other_user}
            return render(request, 'newsfeed.html', dict1)
        else:
            return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        birth_month = request.POST['birth_month']
        birth_day = request.POST['birth_day']
        birth_year = request.POST['birth_year']
        gender = request.POST.get('sex')
        
        # password = base64.encodebytes(password)
        birthday = birth_day + birth_month + birth_year

        if registration.objects.filter(email=email).exists():
                messages.info(request, 'This Email is Taken')
                return redirect('index.html')

        else:
            user = registration(first_name=first_name, last_name=last_name, email=email, password=password, birthday=birthday, gender=gender)
            user.save()
            request.session['email'] = email
            user = registration.objects.filter(email=email, password=password)
            if user.exists():
                other_user = registration.objects.filter().exclude(email=email)
                dict1 = {
                'email': email, 
                'user': user,
                'others': other_user}
                return render(request, 'newsfeed.html', dict1)
            else:
                return render(request, 'index.html')
    else:
        return render(request, 'index.html')


def logout(request):
    del request.session['email']
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
    lng=float(request.GET.get('lng'))
    lat=float(request.GET.get('lat'))
    print(lng)
    print(lat)
    return render(request, 'index.html')

# import geopy.distance as geodist
# def calc_distance(cor1,cor2):
#     distance=geodist.geodesic(cor1, cor2).km
#     print(distance)
