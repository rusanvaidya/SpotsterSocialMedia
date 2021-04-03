from django.shortcuts import render

# Create your views here.
def complete(request):
    return render(request, 'complete.html')