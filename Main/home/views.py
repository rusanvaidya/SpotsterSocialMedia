from django.contrib.auth import login
from django.shortcuts import render
from .models import User_data
from django.core.validators import validate_email
from django.contrib import messages
from django.core.exceptions import ValidationError

def index(request):
    if request.session.get('email') is not  None:
        u_email = request.session.get('email')
        data1 = User_data.objects.filter(email=u_email)
        return render(request,'newsfeed.html',{'u_data':data1})

    return render(request,'index.html')

def home(request):
    process= request.POST.get('status')
    if process == 'signup':
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        birthday = request.POST.get('birthday')
        gender = request.POST.get('sex')

        try:
            validate_email(email)
            if User_data.objects.filter(email=email).exists():
                messages.add_message(request, messages.INFO,
                                 'Invalid! Email or Email exists already please Enter Correctly !')
                return render(request, 'index.html')

            elif password != repassword:
                messages.add_message(request, messages.INFO, 'Password donot match please Enter Correctly !')
                return render(request, 'index.html')

            else:
                My_data = User_data(first_name=firstname, last_name=lastname,email=email,password=password,birthday=birthday,gender=gender)
                My_data.save()
                request.session['email'] = email
                check2 = User_data.objects.filter(email=email)
                return render(request, 'newsfeed.html',{'u_data':check2})



        except ValidationError:

            messages.add_message(request, messages.INFO,
                                 'Invalid! Email or Email exists already please Enter Correctly !')

            return render(request, 'index.html')

    elif process == 'login':
        emails = request.POST.get('email')
        password = request.POST.get('password')

        try:
            check = User_data.objects.get(email=emails)
            pass1 = check.password
            if pass1 == password:
                request.session['email'] = emails
                check1 = User_data.objects.filter(email = emails)
                return render(request, 'newsfeed.html',{'u_data':check1})
            else:
                messages.add_message(request, messages.INFO,
                                     'Invalid! Email or Password please Enter Correctly !')
                return render(request, 'index.html')

        except:
            messages.add_message(request, messages.INFO,
                                 'Invalid! Email or Email not registered please Enter Correctly !')
            return render(request, 'index.html')



    else:
        return render(request, 'index.html')



def profile(request):
    return render(request,'profile.html')



def logout(request):
    if request.session.has_key('email'):
        del request.session['email']
    return render(request,'index.html')
