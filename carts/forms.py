from django import forms

from items.forms import QtyForm

class CartItemQtyForm(QtyForm):
  
  def __init__(self, *args, **kwargs):
    super(CartItemQtyForm, self).__init__(*args, **kwargs)
    self.fields['qty'] = forms.ChoiceField(
      choices=self.find_number_choices(),
      widget=forms.Select(attrs={'onchange': 'form.submit();'}))
