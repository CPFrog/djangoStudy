import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def sub(value, arg):
    return value - arg


# 마크 다운 적용하는 코드
@register.filter()
def mark(value):
    extensions = ['nl2br', 'fenced_code']
    return mark_safe(markdown.markdown(value, extensions=extensions))

# 마크다운 적용 후 작성한 결과
# 1. 1. 1. 식으로 해도 넘버링 적용 안됨
# > 적용 안됨.

