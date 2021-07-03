from django.shortcuts import render
from home.models import registration
# Create your views here.

def chatbox(request):
    email = request.session['email']
    user = registration.objects.filter(email=email)
    return render(request, 'chatbox.html',{'email':email, 'user':user})

def room(request, room_name):
    email = request.session['email']
    user = registration.objects.filter(email=email)
    return render(request, 'chatbox.html', {
        'room_name': room_name,
        'email':email,
        'user':user})
