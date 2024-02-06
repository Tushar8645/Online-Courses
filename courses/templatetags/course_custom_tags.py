import math
from django import template


register = template.Library()


@register.simple_tag
def sellPrice(price, discount):
    if discount is None or discount == 0:
        return price

    sell_price = price - (price * discount * 0.01)

    return math.floor(sell_price)


@register.filter(name='currencySymbol')
def currencySymbol(value):
    return '₹ {}'.format(value)
