# teacher/templatetags/custom_filters.py

from django import template
from django.forms.widgets import Widget

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """
    Returns the value from a dictionary for the given key.
    """
    return dictionary.get(key)

@register.filter
def default_if_none(value, default=""):
    """
    Returns the value or a default if the value is None.
    """
    return value if value is not None else default

@register.filter
def attr(obj, attr_name):
    """
    Gets an attribute from an object if it exists, otherwise returns None.
    """
    return getattr(obj, attr_name, None)

@register.filter(name='add_class')
def add_class(value, css_class):
    """
    Adds a CSS class to a form field if it's a Widget, otherwise returns the value.
    """
    if isinstance(value, Widget):
        return value.as_widget(attrs={"class": css_class})
    else:
        return value
