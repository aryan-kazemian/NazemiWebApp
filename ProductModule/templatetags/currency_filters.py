from django import template

register = template.Library()

@register.filter(name='three_digits_currency')
def three_digits_currency(value):
    """Formats a number with commas and adds 'تومان'."""
    try:
        return '{:,}'.format(int(value)) + ' تومان'
    except (ValueError, TypeError):
        return value  # Return unchanged if conversion fails

