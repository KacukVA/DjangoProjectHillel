from django.core.management.base import BaseCommand
from courses.models import Student, Group
from names import get_first_name, get_last_name
from random import randrange


class Command(BaseCommand):
    help = 'Generates {students_number} students'

    def add_arguments(self, parser):
        parser.add_argument('students_number', nargs='+', type=int)

    def handle(self, *args, **options):
        for _ in range(options['students_number'][0]):
            student = Student(
                first_name=get_first_name(),
                last_name=get_last_name(),
                age=randrange(19, 125),
                group=Group.objects.all().order_by('?')[:1][0],
            )
            student.save()

        self.stdout.write(self.style.SUCCESS(f'Generated {options["students_number"]} students.'))
