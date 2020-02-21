from django.http import HttpResponse
from django.shortcuts import render

def first(request):
    return HttpResponse("Hello! It's first page!")

def articles(request):
    return HttpResponse("It's articles page!")

def archive(request):
    return HttpResponse("It's archive page!")

def users(request):
    users = HttpResponse("")
    users.write("<p><b>It's users page!</b></p><br><p>Vasya</p><p>Zhora</p><p>Masha</p>")
    return users

def article_num(request,article_number):
    return HttpResponse(f"It's article page! Article number is {article_number}!")

def archive_num(request,article_number):
    return HttpResponse(f"<p>It's archive page! Obviously this article in archive!</p> <p>Article number is {article_number}!</p>")

def user_name(request,user_name):
    return HttpResponse(f"<p>It's user's page!</p><p>As you can see in link he/she is {user_name}.</p>")