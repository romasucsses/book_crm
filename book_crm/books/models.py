from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Book(models.Model):
    book_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.IntegerField()
    year = models.IntegerField()
    author = models.CharField(max_length=55)
    in_stock = models.BooleanField(default=True)
    time_added = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="img/%Y/%m/%d/%h/")
    shelf = models.IntegerField()
    slug = models.SlugField(max_length=455, db_index=True, unique=True, verbose_name='URL')

    # auto generation and saved slug for book
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.book_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.book_name

    def get_absolute_url(self):
        return reverse('book_slug_post', kwargs={'book_slug': self.slug})


class Future(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title






