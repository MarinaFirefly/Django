import random
import string
from django.shortcuts import render


def index(request):
    article_id = random.randint(1,3)
    slug = ''
    for i in range(0,10):
        i = random.choice(string.ascii_lowercase + '-')
        slug += i
    return render(request,'index.html',{
        'article_id':article_id,
        'slug':slug,
    })

def first(request):
    return render(request,'first.html')

def article(request,article_id):
    return render(request,f'articles/{article_id}.html',{
        'article_id':article_id,
    })

def slug_rand(request,slug):
    return render(request,'article.html',{
        'slug':slug
    })
