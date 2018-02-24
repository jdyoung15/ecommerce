from django import forms

from .models import InventoryItem

class QtyForm(forms.Form):

  def __init__(self, *args, **kwargs):
    self.item_id = kwargs.pop('item_id', None)
    super(QtyForm, self).__init__(*args, **kwargs)
    self.fields['qty'] = forms.IntegerField(min_value=0, max_value=self.find_max_qty())

  #qty = forms.IntegerField(min_value=0)

  def clean_qty(self):
    qty = self.cleaned_data['qty']
    max_qty = self.find_max_qty()
    if qty > max_qty:
      raise forms.ValidationError("Qty cannot exceed {}!".format(max_qty))
    return qty 

  def find_max_qty(self):
    inventory_item = InventoryItem.objects.filter(item_id=self.item_id).first()
    return inventory_item.qty
    
    
