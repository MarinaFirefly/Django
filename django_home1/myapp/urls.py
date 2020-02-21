from django.contrib import admin
from django.urls import path
from .views import archive, archive_num, article_num, articles, first, user_name, users

urlpatterns = [
    path('', first, name="index"),
    path('articles/', articles),
    path('articles/archive/', archive),
    path('users/', users),
    path('article/<int:article_number>', article_num),
    path('article/<int:article_number>/archive', archive_num),
    path('user/<str:user_name>', user_name),
]
