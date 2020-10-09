"""mysite URL Configuration

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
from myapp.views import index, articles, archive, users, article_number, archive_number, users_number

urlpatterns = [
    # path('my_url/', include('myapp.urls')),
    path('', index, name='index'),
    path('articles/', articles, name='articles'),
    path('articles/archive', archive, name='archive'),
    path('users', users, name='users'),
    path('article/<int:article_number>', article_number, name='article_number'),
    path('http://127.0.0.1:8000/article/<int:article_number>/archive', archive_number, name='archive_number'),
    path('users/<int:users_number>', users_number, name='users_number')
]