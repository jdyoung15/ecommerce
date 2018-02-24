from django import forms

from .models import InventoryItem

class QtyForm(forms.Form):
  qty = forms.IntegerField(min_value=0)

  def __init__(self, *args, **kwargs):
    self.item_id = kwargs.pop('item_id', None)
    super(QtyForm, self).__init__(*args, **kwargs)

  def clean_qty(self):
    qty = self.cleaned_data['qty']
    item_id = self.item_id
    inventory_item = InventoryItem.objects.filter(item_id=item_id).first()
    if qty > inventory_item.qty:
      raise forms.ValidationError("Qty cannot exceed {}!".format(inventory_item.qty))

    return qty 
