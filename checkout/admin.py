from django.contrib import admin
from .models import Order, OrderLineItem
from django.db.models import Sum
from django.conf import settings

class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_cart',
                       'stripe_pid')

    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total', 'original_cart',
              'stripe_pid')

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-date',)

    def delivery_cost(self, obj):
        return obj.delivery_cost

    def order_total(self, obj):
        return obj.order_total

    def grand_total(self, obj):
        return obj.grand_total

    delivery_cost.short_description = 'Delivery Cost'
    order_total.short_description = 'Order Total'
    grand_total.short_description = 'Grand Total'

admin.site.register(Order, OrderAdmin)
