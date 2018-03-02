from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse

from items.models import Item, InventoryItem


def create_test_item(item_name):
  return Item.objects.create(name=item_name, price=1, msrp=2, description="Test item description")

class ItemModelTests(TestCase):

  def test_negative_price(self):
    test_item = Item(name="Test item", price=-1, msrp=2, description="Test item description")
    self.assertRaises(ValidationError, test_item.full_clean)

  def test_positive_msrp(self):
    test_item = Item(name="Test item", price=1, msrp=2, description="Test item description")
    test_item.full_clean()

  def test_zero_qty(self):
    test_item = create_test_item('Test item')
    test_inventory_item = InventoryItem(item_id=test_item.id, qty=0)
    test_inventory_item.full_clean()
  
class ItemIndexViewTests(TestCase):

  def test_no_items(self):
    response = self.client.get(reverse('items:index'))
    self.assertEqual(response.status_code, 200)
    self.assertQuerysetEqual(response.context['item_list'], [])

  def test_multiple_items(self):
    create_test_item('Test item 1')
    create_test_item('Test item 2')
    response = self.client.get(reverse('items:index'))
    self.assertQuerysetEqual(response.context['item_list'], ['<Item: Test item 1>', '<Item: Test item 2>'])

  def test_items_order(self):
    create_test_item('Aa')
    create_test_item('Z')
    create_test_item('A')
    create_test_item('5')
    response = self.client.get(reverse('items:index'))
    self.assertQuerysetEqual(
      response.context['item_list'], 
      ['<Item: 5>', '<Item: A>', '<Item: Aa>', '<Item: Z>'])


class ItemDisplayViewTests(TestCase):

  def test_nonexistent_item(self):
    response = self.client.get(reverse('items:detail', args=(1234,)))
    self.assertEqual(response.status_code, 404)

  def test_existing_item(self):
    item = create_test_item('Test item')
    inventory_item = InventoryItem.objects.create(item_id=item.id, qty=1)
    response = self.client.get(reverse('items:detail', args=(item.id,)))
    print('response {}'.format(response))
    self.assertContains(response, 'Test item')
