from django import template
from django.utils.safestring import mark_safe

import re

register = template.Library()

@register.filter
def highlight(text, word):
    highlighted_text = re.sub(r'\b({})\b'.format(word), r'<span class="highlight">\1</span>', text, flags=re.IGNORECASE)
    return mark_safe(highlighted_text)
