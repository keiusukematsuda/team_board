from django import template
register = template.Library()

@register.filter(name='counter')
def counter(dates):
    print(dates.filter(Attend="1"))
    return ""
