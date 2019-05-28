from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def bootstrap_css():
    tags = [
    '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">',
    '<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>'
    ]
    return ''.join(tags)

@register.inclusion_tag('bootstrap_button.html')
def bootstrap_button(text, style="default"):
    return {
        'style': style.lower(),
        'text': text,
        }