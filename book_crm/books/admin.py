from django.contrib import admin

from books.models import Book, Future
from clients.models import Client
from orders.models import Order

admin.site.register(Book)
admin.site.register(Future)
admin.site.register(Client)
admin.site.register(Order)
