from django.urls import path
from .views import registration_view,follow_setup,login_user

urlpatterns = [
    path('userdata/',registration_view),
    path('userfollowsetup/',follow_setup),
    path('userlogin/',login_user),
]