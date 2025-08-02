from django.db import models

class Inventory(models.Model):
    Material = models.CharField(max_length=10)
    Finish = models.CharField(max_length=5)
    Length = models.IntegerField()
    Price_per_length = models.IntegerField()
    Order_info = models.CharField(max_length=200)
    coil_number = models.IntegerField()
    order_number = models.ForeignKey(
        'customer_module.Order',
        on_delete=models.CASCADE,
        related_name='inventory_items',
        blank=True,
        null=True
    )
    STATUS_CHOICES = [
        ('To be created', 'To be created'),
        ('Created', 'Created'),
        ('Shipped', 'Shipped'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='To be created')
    
    def price(self):
        return self.Length * self.Price_per_length
