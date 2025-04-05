from django import template
import json
from django.utils.translation import gettext_lazy as _

register = template.Library()


@register.filter
def format_timedelta(value):
    timetot = ""
    if value:
        days = value.days
        hours, rem = divmod(value.seconds, 3600)
        minutes, seconds = divmod(rem, 60)
        if days > 0:
            timetot += _('%(n_days)s days') % {'n_days': days}
        if hours > 0:
            timetot += ' {} hours'.format(hours)
        if minutes > 0:
            timetot += ' {}min'.format(minutes)
        return timetot
    return _('Check duration')


@register.filter
def times(number):
    return range(int(number))

@register.filter
def first_index(item):
    return item[0]

@register.filter
def string_value(value):
    return str(value)

@register.filter
def choose_index(item, index):
    return item[:index]

@register.filter
def second_index(item):
    return item[1]


@register.filter
def to_json(value):
    return json.dumps(value)


@register.simple_tag
def variable_true():
    """Pone una variable a True, para forloop con condiciones."""
    return True


@register.simple_tag
def get_preference(key):
    from ..models import SitePreference
    return SitePreference.get_preference(key)


@register.simple_tag(takes_context=True)
def param_replace(context, **kwargs):
    """
    Funcion que devuelve los paramentros GET de la url y sustituye los que le pasemos
    :param context:
    :param kwargs:
    :return:
    """
    d = context['request'].GET.copy()
    for k, v in kwargs.items():
        d[k] = v
    for k in [k for k, v in d.items() if not v]:
        del d[k]
    return d.urlencode()

@register.filter
def capitalize(value):
    return str(value).title()