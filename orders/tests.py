from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse

from items.models import Item, InventoryItem
from orders.models import Order, OrderUpdate, OrderItem


#def create_test_item(item_name):
#  return Item.objects.create(name=item_name, price=1, msrp=2, description="Test item description")
#
#class ItemModelTests(TestCase):
#
#  def test_negative_price(self):
#    test_item = Item(name="Test item", price=-1, msrp=2, description="Test item description")
#    self.assertRaises(ValidationError, test_item.full_clean)
#
#  def test_positive_msrp(self):
#    test_item = Item(name="Test item", price=1, msrp=2, description="Test item description")
#    test_item.full_clean()
#
#  def test_zero_qty(self):
#    test_item = create_test_item('Test item')
#    test_inventory_item = InventoryItem(item_id=test_item.id, qty=0)
#    test_inventory_item.full_clean()
  
#class ItemIndexViewTests(TestCase):
#
#  def test_no_items(self):
#    response = self.client.get(reverse('items:index'))
#    self.assertEqual(response.status_code, 200)
#    self.assertQuerysetEqual(response.context['item_list'], [])
#
#  def test_multiple_items(self):
#    create_test_item('Test item 1')
#    create_test_item('Test item 2')
#    response = self.client.get(reverse('items:index'))
#    self.assertQuerysetEqual(response.context['item_list'], ['<Item: Test item 1>', '<Item: Test item 2>'])
#
#  def test_items_order(self):
#    create_test_item('Aa')
#    create_test_item('Z')
#    create_test_item('A')
#    create_test_item('5')
#    response = self.client.get(reverse('items:index'))
#    self.assertQuerysetEqual(
#      response.context['item_list'], 
#      ['<Item: 5>', '<Item: A>', '<Item: Aa>', '<Item: Z>'])


class OrderCreateViewTests(TestCase):

  def test_valid_order(self):
    data = {
      'email': 'test@test.com',
      'form-TOTAL_FORMS':	'2',
      'form-INITIAL_FORMS':	'0',
      'form-MIN_NUM_FORMS':	'0',
      'form-MAX_NUM_FORMS':	'1000',
      'form-0-name': 'Shipping Name',
      'form-0-line_one': '1234 Shipping St',
      'form-0-line_two': 'Apt 1',
      'form-0-city': 'Shipping City',
      'form-0-state': 'SS',
      'form-0-zip_code': '12345',
      'form-0-country': 'US',
      'form-0-phone': '5551234567',
      'form-0-id': '',
      'form-1-name': 'Billing Name',
      'form-1-line_one': '1234 Billing St',
      'form-1-line_two': 'Apt 2',
      'form-1-city': 'Billing City',
      'form-1-state': 'BS',
      'form-1-zip_code': '67890',
      'form-1-country': 'US',
      'form-1-phone': '5559876543',
      'form-1-id': '',
    }
    response = self.client.post(reverse('orders:new'), data=data)
    self.assertEqual(response.status_code, 302)

    order = Order.objects.get(pk=1)
    self.assertEqual(order.customer.email, 'test@test.com')
    self.assertEqual(order.customer.shipping_address.name, 'Shipping Name')
    self.assertEqual(order.customer.shipping_address.line_one, '1234 Shipping St')
    self.assertEqual(order.customer.shipping_address.line_two, 'Apt 1')
    self.assertEqual(order.customer.shipping_address.city, 'Shipping City')
    self.assertEqual(order.customer.shipping_address.state, 'SS')
    self.assertEqual(order.customer.shipping_address.zip_code, '12345')
    self.assertEqual(order.customer.shipping_address.country, 'US')
    self.assertEqual(order.customer.shipping_address.phone, '5551234567')
    self.assertEqual(order.customer.billing_address.name, 'Billing Name')
    self.assertEqual(order.customer.billing_address.line_one, '1234 Billing St')
    self.assertEqual(order.customer.billing_address.line_two, 'Apt 2')
    self.assertEqual(order.customer.billing_address.city, 'Billing City')
    self.assertEqual(order.customer.billing_address.state, 'BS')
    self.assertEqual(order.customer.billing_address.zip_code, '67890')
    self.assertEqual(order.customer.billing_address.country, 'US')
    self.assertEqual(order.customer.billing_address.phone, '5559876543')

    # TODO: order items?

    # TODO implement shipping calculation
    self.assertEqual(order.shipping, 5)

    order_update = order.orderupdate_set.first()
    self.assertEqual(order_update.status, OrderUpdate.PROCESSING)



  #def test_nonexistent_item(self):
  #  response = self.client.get(reverse('items:detail', args=(1234,)))
  #  self.assertEqual(response.status_code, 404)

  #def test_existing_item(self):
  #  item = create_test_item('Test item')
  #  inventory_item = InventoryItem.objects.create(item_id=item.id, qty=1)
  #  response = self.client.get(reverse('items:detail', args=(item.id,)))
  #  print('response {}'.format(response))
  #  self.assertContains(response, 'Test item')
