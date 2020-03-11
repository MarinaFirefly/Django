"""django_home6 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from bookapp.views import Index, BookCreateView, BookUpdateView, BookDeleteView, BookDetailView, BookListView, CommentsListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book_create/', BookCreateView.as_view(), name='book_create'),
    path('book_update/<int:pk>/', BookUpdateView.as_view(), name='book_update'),
    path('book_delete/<int:pk>/', BookDeleteView.as_view(), name='book_delete'),
    path('book_detail/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('book_list/', BookListView.as_view(), name='book_list'),
    path('comments/', CommentsListView.as_view(), name='comments'),
    path('', Index.as_view(), name='index'),
]
