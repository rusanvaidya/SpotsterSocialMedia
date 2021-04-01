from django.urls import path
from.views import user_account

urlpatterns = [
    path('userdata/',user_account),
]