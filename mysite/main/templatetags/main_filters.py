from django import template

register = template.Library()


@register.filter(name='discount')
def get_discount(price, discount):
    return price * (1 - discount / 100)


@register.filter(name='goods_on_page')
def show_goods_range(page_obj):
    start = (page_obj.number - 1) * page_obj.paginator.per_page + 1
    end = page_obj.number * page_obj.paginator.per_page
    end = end if end < page_obj.paginator.count else page_obj.paginator.count
    return f"Showing {start} - {end} of {page_obj.paginator.count} result"
