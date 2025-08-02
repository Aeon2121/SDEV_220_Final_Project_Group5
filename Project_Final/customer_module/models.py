'''from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from inventory_module.models import Inventory
from online_ordering import Customer

class Order(models.Model):
    Customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null = False)
    Order_Number = models.IntegerField(unique = True, null = False)
    Order_Info = models.CharField(max_length=200, null = False)
    Order_date = models.DateTimeField(blank=True, null=True)

    def set_customer(self):
        self.Customer = Customer.__name__

    def set_order_number(self):
        self.Order_Number = Inventory.Order_Number

    def set_order_info(self):
        self.Order_Info = Inventory.Order_info

    def publish(self):
        self.order_date = timezone.now()
        self.save()

    def __init__(self):
        self.set_customer()
        self.set_order_info()
        self.set_order_number()
        '''


from django.conf import settings
from django.db import models
from django.utils import timezone
from inventory_module.models import Inventory

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

    def publish(self):
        self.order_date = timezone.now()
        self.save()

    def __str__(self):
        return f"Order #{self.order_number} by {self.customer}"
