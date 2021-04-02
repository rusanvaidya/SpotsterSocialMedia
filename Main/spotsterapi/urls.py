from django.urls import path
from .views import registration_view,login_user,follow_setup

urlpatterns = [
    path('userdata/',registration_view),
    path('userfollowsetup/',follow_setup),
    path('userlogin/',login_user),
]