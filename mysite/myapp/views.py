from django.shortcuts import render
from django.http import HttpResponse
#
# def first(request):
#     return HttpResponse("Hey! It's your first view!!")

def index(request):
    return HttpResponse("It's index page!")

def articles(request):
    return HttpResponse("Articles are here")

def archive(request):
    return HttpResponse('Here is the archive of articles')

def users(request):
    return HttpResponse('Users are here')

def article_number(request, article_number):
    return HttpResponse('This is the article {}'.format(article_number))

def archive_number(request, article_number):
    return HttpResponse('This is the article {}'.format(article_number) + ' from archive')

def users_number(request, users_number):
    return HttpResponse('This is the user number {}'.format(users_number))

# Create your views here.
