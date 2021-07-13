"""Main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home,name='home'),
    path('login', views.login),
    path('register', views.register),
    path('content_post', views.user_post,name='user_post'),
    path('logout', views.logout),
    path('support',views.support_view,name='supportpage'),
    path('notification', views.notification),
    path('post_comment', views.post_comment,name='post_comment'),
    path('comment_post', views.comment_post,name='comment_post'),
    path('like_unlike',views.like_post),
    path('delete_comment',views.delete_comment,name='delete_comment'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)