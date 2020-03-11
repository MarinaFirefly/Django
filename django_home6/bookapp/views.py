from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView
from django.urls import reverse_lazy
from .forms import BooksForm, SearchBoxForm, OrderingForm
from .models import Book, Comment


class Index(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'param_a': 'Comments',
            'param_b': 'Books',
        })
        return context


class BookCreateView(CreateView):
    model = Book
    template_name = 'book_create.html'
    form_class = BooksForm
    success_url = reverse_lazy('book_create')


class BookUpdateView(UpdateView):
    model = Book
    template_name = 'book_update.html'
    success_url = ('/')
    fields = ['article', 'author', 'text']


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_delete.html'
    success_url = reverse_lazy('book_list')


class BookDetailView(DetailView):
    model = Book


class BookListView(ListView):
    model = Book
    paginate_by = 10
    template_name = 'book_list.html'
    queryset = Book.objects.all()
    def get_queryset(self):
        search = self.request.GET.get('Article')
        order = self.request.GET.get('order')
        if search:
            query = Q(article__icontains=search)
            return Book.objects.filter(query)
        if order in ['article', 'author']:
            return Book.objects.order_by(order)
        else:
            return Book.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {'search_form': SearchBoxForm,
             'ordering_form': OrderingForm})
        return context


class CommentsListView(ListView):
    model = Comment
    paginate_by = 10
    template_name = 'comments.html'
    queryset = Comment.objects.all()
