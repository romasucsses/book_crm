from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=155)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=555)
    time_joining = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


    # @staticmethod
    # def total_sum_orders():
    #     suma = 0
    #     allot = Order.objects.all()
    #     for each in allot:
    #         suma += int(each.cost_per_product)
    #     return suma
    #
    # total_orders = total_sum_orders()







