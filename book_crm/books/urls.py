from django.urls import path
from .views import*
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Home.as_view(), name='all_books'),
    path('add_book/', AddBook.as_view(), name='add_book'),
    path('future_books/', FutureBook.as_view(), name='future_books'),
    path('<slug:book_slug>/', BookSlug.as_view(), name='book_slug_post')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)