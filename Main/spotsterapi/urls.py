from django.urls import path
from .views import registration_view

urlpatterns = [
    path('userdata/',registration_view),
]