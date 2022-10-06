from django.views.generic import TemplateView
from courses.models import Student, Group, Teacher


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        print(
            # Вивести всіх студентів
            Student.objects.all(),
            # Вивести всі группи
            Group.objects.all(),
            # Вивести всіх вчетелів
            Teacher.objects.all(),
            # Вивести всіх студентів для однієї групи
            Student.objects.filter(group_id=1),
            # Вивести всіх студентів для одного викладача
            Student.objects.prefetch_related('group__teacher_set').filter(group__teacher=1),
            # Вивести усіх студентів чий вік більше 20
            Student.objects.filter(age__gt=20),
            # Вивести усіх студентів для одного викладача чий вік більше 20
            Student.objects.prefetch_related('group__teacher_set').filter(group__teacher=1, group__teacher__age__gt=20),
            # Вивести усіх студентів у яких email на домені gmail.com
            Student.objects.filter(email__contains='gmail'),
            sep='\n'
        )
        return context
