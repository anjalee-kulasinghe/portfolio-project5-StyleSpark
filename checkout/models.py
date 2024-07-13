from django.db import models
from django_countries.fields import CountryField
from products.models import Product
from profiles.models import UserProfile
import uuid

class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    rental_start_date = models.DateField(null=False, blank=False)
    rental_end_date = models.DateField(null=False, blank=False)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    original_cart = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)
        self.update_totals()

    def update_totals(self):
        """
        Update order total and grand total based on line items and delivery cost.
        """
        rental_duration = (self.rental_end_date - self.rental_start_date).days + 1
        self.order_total = sum(item.calculate_lineitem_total(rental_duration) for item in self.lineitems.all())
        self.grand_total = self.order_total + self.delivery_cost
        self.save(update_fields=['order_total', 'grand_total'])

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    product_size = models.CharField(max_length=2, null=True, blank=True)  # XS, S, M, L, XL
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        rental_duration = (self.order.rental_end_date - self.order.rental_start_date).days + 1
        self.lineitem_total = self.calculate_lineitem_total(rental_duration)
        super().save(*args, **kwargs)
        self.order.update_totals()

    def calculate_lineitem_total(self, rental_duration):
        return self.product.price * self.quantity * rental_duration

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'
