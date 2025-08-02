from django import forms
from .models import Inventory

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['Material', 'Finish', 'Length', 'Price_per_length', 'Order_info', 'order_number', 'coil_number', 'status']
