from django import template
from django.db.models import Count, Sum

from courses.models import Course, Student, Group

register = template.Library()


@register.filter()
def get_doubles(text):
    pass


@register.filter()
def word_count(text):
    pass


@register.inclusion_tag('includes/course_list.html')
def get_favorites():
    # result = Student.objects.values_list('group__course__name').annotate(course_count=Count('group__course')).order_by('-course_count')[:5]
    # print(result)
    return {
        'favorites': Student.objects.values('group__course__name').annotate(course_count=Count('group__course')).order_by('-course_count')[:5]
    }
