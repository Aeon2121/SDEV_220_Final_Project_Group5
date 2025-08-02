from django.conf import settings
from django.db import models
from django.utils import timezone
from inventory_module.models import Inventory

'''
from ...online_ordering import Customer 
from ...online_ordering import Order as online_order #v1

from sales_module import OrderSys1 #v2
'''

class Order(models.Model):
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='orders'
    )
    inventory_item = models.ForeignKey(
        Inventory,
        on_delete=models.CASCADE,
        related_name='orders'
    )
    order_number = models.IntegerField(unique=True)
    order_info = models.CharField(max_length=200)
    order_date = models.DateTimeField(blank=True, null=True)
    customer_name = models.CharField(max_length=100)

    def publish(self):
        self.order_date = timezone.now()
        self.save()

    '''
    def set_customer_name(self):
        self.customer_name = Customer.__name__

    def set_order_number(self):
        self.Order_Number = online_order.order_counter

    def set_order_info(self):
        self.Order_Info = str(online_order.items + online_order.status) #v1
        self.Order_Info = OrderSys1.orders[self.order_number] #v2
    def __init__(self):
        self.set_order_info()
        self.set_order_number()
        self.set_customer_name()
    '''
        
    def __str__(self):
        return f"Order #{self.order_number} by {self.customer}"
