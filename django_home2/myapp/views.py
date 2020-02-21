import random
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def first(request):
    return render(request,'first.html')

def article(request,article_id):
    article_id = random.randint(1,3)
    return render(request,f'articles/{article_id}.html',{
        'article_id':article_id,
    })

def slug_rand(request,slug):
    slug = 'qw'
    return render(request,'article.html',{
        'slug':slug
    })