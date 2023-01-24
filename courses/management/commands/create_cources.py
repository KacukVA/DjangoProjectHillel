from django.core.management.base import BaseCommand
from courses.models import Course, Teacher, Category
from random import choice


class Command(BaseCommand):
    help = 'Generates {curses_number} courses'

    def add_arguments(self, parser):
        parser.add_argument('curses_number', nargs='+', type=int)

    def handle(self, *args, **options):
        prefixes = ['Super', 'Mega', 'Greatest', 'Best']
        languages = ['Python', 'Java', 'PHP', 'Kotlin', 'JavaScript']
        course_count = int(Course.objects.all().count())
        for _ in range(options['curses_number'][0]):
            course_count += 1
            course = Course(
                name=f'{choice(prefixes)} {choice(languages)} course №{course_count}',
                description='Some description',
                thesis='Some theses',
                category=Category.objects.all().order_by('?')[:1][0],
                teacher=Teacher.objects.all().order_by('?')[:1][0],
            )
            course.save()

        self.stdout.write(self.style.SUCCESS(f'Generated {options["curses_number"]} courses.'))
