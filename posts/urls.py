"""blogs URL Configuration

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
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.post_list, name='list'),
    path('create', views.post_create),
    re_path(r'^(?P<id>\d+)/$', views.post_detail, name='detail'),
    re_path(r'^(?P<id>\d+)/edit/$', views.post_update, name='update'),
    re_path(r'^(?P<id>\d+)/delete/$', views.post_delete),
]

app_name = 'posts'
