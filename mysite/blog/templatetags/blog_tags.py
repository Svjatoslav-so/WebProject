from django import template

from ..models import Tag

register = template.Library()


@register.simple_tag()
def all_post_tags():
    return Tag.objects.all()
