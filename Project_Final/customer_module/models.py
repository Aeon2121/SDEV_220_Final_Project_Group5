from django.conf import settings
from django.db import models
from django.utils import timezone
from inventory_module import models as Inventory

class Order(models.Model):
    Customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, unique = True, null = False)
    Order_Number = models.IntegerField(max_length=25, unique = True, null = False)
    Order_Info = Inventory.models.CharField(max_length=200)
    Order_date = models.DateTimeField(default=timezone.now, unique = True, null = False)

    def Order(self):
        self.Order_date = timezone.now()
        self.save()

    def __str__(self):
        return self.Order_Number
# Create your models here.
