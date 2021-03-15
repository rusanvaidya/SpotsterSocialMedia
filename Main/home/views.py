from django.shortcuts import render,redirect
from .models import support

# Create your views here.
def home(request):
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
