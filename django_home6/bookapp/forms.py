from django import forms
from .models import Book


class BooksForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['article', 'author', 'text']


class SearchBoxForm(forms.Form):
    Article = forms.CharField()


ORDER = (
    ('author', 'By author'),
    ('article', 'By name')
)


class OrderingForm(forms.Form):
    order = forms.ChoiceField(choices=ORDER)
    