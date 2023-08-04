from django import forms
from django.core.exceptions import ValidationError

from books.models import Book, Future


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'book_name',
            'description',
            'price',
            'year',
            'author',
            'image',
            'shelf'
        ]

    def clean_book_name(self):
        book_name = self.cleaned_data['book_name']
        if Book.objects.filter(book_name=book_name).exists():
            raise ValidationError('Book already exist, please enter other book')

        return book_name


class AddFutureBookForm(forms.ModelForm):
    class Meta:
        model = Future
        fields = ['title', 'author']


