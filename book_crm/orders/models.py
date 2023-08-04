from django.db import models


class Order(models.Model):
    customer_information = models.ForeignKey('clients.Client', on_delete=models.PROTECT)
    book = models.ManyToManyField('books.Book')
    delivery = models.IntegerField(default=30)

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('delivered', 'Delivered'),
        ('canceled', 'Canceled'),
    )
    status = models.CharField(max_length=55, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    date_for_delivery = models.DateField()

    def calculate_cost_per_product(self):
        return sum(self.book.values_list('price', flat=True))

    def __str__(self):
        return str(self.pk)


