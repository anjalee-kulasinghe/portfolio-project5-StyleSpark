from django import template

register = template.Library()

@register.simple_tag
def calc_subtotal(price, quantity, rental_days):
    """Calculate the subtotal."""
    try:
        return price * quantity * rental_days
    except (TypeError, ValueError):
        return 0