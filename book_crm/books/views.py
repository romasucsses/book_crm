from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from books.models import Book, Future
from books.forms import AddBookForm, AddFutureBookForm
from mixins.mixin_global import CurrentPageContext


class Home(CurrentPageContext, ListView):
    model = Book
    template_name = 'books/index.html'
    context_object_name = 'books'
    paginate_by = 8
    ordering = 'pk'
    # mixin info
    mixin_page_name = 'all_books'


class AddBook(CurrentPageContext, CreateView):
    form_class = AddBookForm
    template_name = 'books/add_book.html'
    success_url = reverse_lazy('all_books')
    # mixin info
    mixin_page_name = 'add_book'


class BookSlug(CurrentPageContext, DetailView):
    model = Book
    template_name = 'books/slug_book.html'
    context_object_name = 'post'
    slug_field = 'slug'
    slug_url_kwarg = 'book_slug'
    # mixin info
    mixin_page_name = 'book_slug_post'

    def get_queryset(self):
        return super().get_queryset().filter(slug=self.kwargs['book_slug'])

    def get_post(self):
        return get_object_or_404(self.get_queryset())

    def post(self, request, book_slug):
        action = request.POST.get('action')
        if action == 'book_delete':
            return self.delete_book(request, book_slug)

    def delete_book(self, request, book_slug):
        book = get_object_or_404(Book, slug=book_slug)
        book.delete()
        return redirect('all_books')


class FutureBook(CurrentPageContext, ListView):
    model = Future
    template_name = 'books/future.html'
    context_object_name = 'future'
    paginate_by = 4
    ordering = 'pk'
    # mixin info
    mixin_page_name = 'future_books'

    def get(self, request, *args, **kwargs):
        action = request.GET.get('action')
        if action == "search-request":
            return self.search(request)
        return super().get(request, *args, **kwargs)

    def post(self, request):
        action = request.POST.get('action')
        if action == 'del_book':
            return self.del_book(request)
        if action == 'add_future_book':
            return self.add_future_book(request)

    def del_book(self, request):
        id = request.POST.get('pk')
        book = Future.objects.filter(pk=id)
        book.delete()
        return redirect('future_books')

    def add_future_book(self, request):
        form = AddFutureBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('future_books')
        else:
            future = Future.objects.all()
            return render(request, 'books/future.html', {'future': future})

    def search(self, request):
        query = request.GET.get('q')
        if query:
            books = Future.objects.filter(title__icontains=query)
        else:
            books = Future.objects.all()

        return render(request, 'books/future.html', {'books': books})
