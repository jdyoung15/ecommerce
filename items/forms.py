from django import forms

from .models import InventoryItem

#TODO: rename to ItemQtyForm
class QtyForm(forms.Form):
  
  MIN_QTY = 1

  def __init__(self, *args, **kwargs):
    self.item_id = kwargs.pop('item_id', None)
    super(QtyForm, self).__init__(*args, **kwargs)
    self.fields['qty'] = forms.ChoiceField(self.find_number_choices())


  def find_number_choices(self):
    start = self.MIN_QTY
    end = self.find_max_qty()
    zipped = zip(*[range(start, end + 1)] * 2)
    return [t for t in zipped]


  def find_max_qty(self):
    inventory_item = InventoryItem.objects.filter(item_id=self.item_id).first()
    return inventory_item.qty
