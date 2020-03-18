from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView, FormView, ListView, DeleteView, TemplateView, View, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from shop_app.forms import RegistrationForm, LoginForm, ProductForm, PurchaseForm
from shop_app.models import Product, Purchase


class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'param_a': 'Coffee Shop',
        })
        return context


class Registration(CreateView):
    # model = Customer
    form_class = RegistrationForm
    template_name = 'registration.html'
    success_url = '/'


class Login(FormView):
    form_class = LoginForm
    success_url = '/'
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
        return redirect('/')


class Logout(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        logout(request.user)
        # return super().get(request, *args, **kwargs)
        return HttpResponseRedirect("/")


class ProductListView(ListView):
    model = Product
    paginate_by = 2
    template_name = 'products_list.html'
    queryset = Product.objects.all()
    ordering = ['title']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {'purchase_form': PurchaseForm,
             })
        return context


class ProductCreateView(CreateView):
    model = Product
    template_name = 'product_create.html'
    form_class = ProductForm
    success_url = reverse_lazy('product_create')


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product_update.html'
    success_url = '../../products_list'
    fields = ['picture', 'title', 'text', 'price', 'quantity']


class PurchaseCreateView(CreateView):
    http_method_names = ['post', ]
    success_url = reverse_lazy('products_list/')
    model = Purchase
    form_class = PurchaseForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.customer = self.request.user
        obj.product = self.object.Product
        self.object = obj.save()
        return super().form_valid(form)


