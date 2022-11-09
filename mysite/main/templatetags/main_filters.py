from django import template

register = template.Library()


@register.filter(name='discount')
def get_discount(price, discount):
    return price*(1-discount/100)
