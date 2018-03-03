from django.db import models
from django.core.validators import MinValueValidator

class Address(models.Model):
  name = models.CharField(max_length=100)
  line_one = models.CharField(max_length=100)
  line_two = models.CharField(max_length=100)
  city = models.CharField(max_length=50)
  state = models.CharField(max_length=2)
  zip_code = models.CharField(max_length=20)
  country = models.CharField(max_length=50)
  phone = models.CharField(max_length=50)
  is_default = models.BooleanField(default=False)
  
  def __str__(self):
    return '{}\n{}\n{}\n{} {} {}\n{}\n{}'.format(
      self.name, self.line_one, self.line_two, self.city, self.state, self.zip_code, self.country, self.phone)


class Customer(models.Model):
  email = models.EmailField()
  billing_address = models.ForeignKey(Address, on_delete=models.PROTECT, related_name='billingaddress')
  shipping_address = models.ForeignKey(Address, on_delete=models.PROTECT, related_name='shippingaddress')
  #price = models.PositiveIntegerField(validators=[MinValueValidator(0)])
  #msrp = models.PositiveIntegerField(validators=[MinValueValidator(0)])
  #description = models.TextField()
  
  def __str__(self):
    return 'id: {} email: {}'.format(self.id, self.email)

