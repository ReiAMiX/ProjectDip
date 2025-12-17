from django import templates
register = templates.Library()



@register.filter
def mul(value, arg):
    return value * arg