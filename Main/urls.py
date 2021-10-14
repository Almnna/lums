"""lums URL Configuration

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
from . import views as v

urlpatterns = [
    path('',v.index, name="index"),
    path('login', v._login_, name="login"),
    path('panel', v.panel, name="panel"),
    path('logout', v._logout_, name="logout"),
    path('dashboard', v.dashboard, name="dashboard"),
    path('update/<lecture_id>', v._update_, name="update"),
    path('delete/<lecture_id>', v.delete_lecture, name="delete_lecture"),
]
