from django import template

register = template.Library()


@register.inclusion_tag('main/product_small_cart.html')
def show_product(product):
    return {"product": product}
