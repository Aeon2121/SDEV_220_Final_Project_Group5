from django.db import models
from customer_module import models as Order

class Inventory(models.Model):
    # We need the material type, finish, the length, and the price per length of the coils
    Material = models.CharField(max_length=10)
    Finish = models.CharField(max_length=5)
    Length = models.IntegerField()
    Price_per_length = models.IntegerField()
    Order_info = models.CharField(max_length=200)
    Order_Number = models.IntegerField()
    coil_number = models.IntegerField()
    STATUS_CHOICES = [
        ('To be created', 'To be created'),
        ('Created', 'Created'),
        ('Shipped', 'Shipped'),
    ]
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='To be created')
    
    def price(self):
        return self.Length * self.Price_per_length