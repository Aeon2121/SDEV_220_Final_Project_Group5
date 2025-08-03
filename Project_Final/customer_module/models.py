from django.conf import settings
from django.db import models
from django.utils import timezone
from inventory_module.models import Inventory


class Order(models.Model):
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='orders',
        default=""
    )
    inventory_item = models.ForeignKey(
        Inventory,
        on_delete=models.CASCADE,
        related_name='orders'
    )
    order_number = models.IntegerField(unique=True)
    order_info = models.CharField(max_length=200)
    order_date = models.DateTimeField(blank=True, null=True)
    customer_name = models.CharField(max_length=100, default="")

    def publish(self):
        self.order_date = timezone.now()
        self.save()

    def __str__(self):
        return f"Order #{self.order_number} by {self.customer}"
