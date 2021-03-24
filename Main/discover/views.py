from django.shortcuts import render
from home.models import registration
# Create your views here.

def discover(request):
    email = request.session['email']
    user = registration.objects.filter(email=email)
    return render(request, 'discover.html',{'email':email, 'user':user})