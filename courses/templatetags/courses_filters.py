from django import template
from django.db.models import Count
from courses.models import Student
import re

register = template.Library()


@register.filter()
def get_pair(text):
    return [x for x in text if isinstance(x, int) and x % 2 == 0]


@register.filter()
def word_count(text):
    return len(re.findall(r'\w+', text))


@register.inclusion_tag('includes/course_list.html')
def get_favorites():
    return {
        'favorites': Student.objects.values('group__course__name', 'group__course__id').annotate(
            course_count=Count('group__course')).order_by('-course_count')[:5]
    }
