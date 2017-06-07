import random
from django import template
from ..models import Mineral

register = template.Library()


@register.simple_tag
def random_detail():
    mineral = Mineral.objects.all()
    num_minerals = len(mineral)
    random_pk = random.randint(1, num_minerals)
    return str(random_pk)
