from django import forms

from .models import InventoryItem

class QtyForm(forms.Form):
  
  MIN_QTY = 0

  def __init__(self, *args, **kwargs):
    self.item_id = kwargs.pop('item_id', None)
    super(QtyForm, self).__init__(*args, **kwargs)
    self.fields['qty'] = forms.ChoiceField(self.find_number_choices())

  def clean_qty(self):
    qty = int(self.cleaned_data['qty'])
    max_qty = self.find_max_qty()
    if qty > max_qty:
      raise forms.ValidationError("Qty cannot exceed {}!".format(max_qty))
    return qty 

  def find_max_qty(self):
    inventory_item = InventoryItem.objects.filter(item_id=self.item_id).first()
    return inventory_item.qty
    
  def find_number_choices(self):
    start = self.MIN_QTY
    end = self.find_max_qty()
    zipped = zip(*[range(start, end + 1)] * 2)
    return [t for t in zipped]
