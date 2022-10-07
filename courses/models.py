from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class AbstractName(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        abstract = True
        ordering = ['id']

    def __str__(self):
        return self.name


class Group(AbstractName):
    pass


class Person(AbstractName):
    age = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(125),
            MinValueValidator(1)  # 1 т.к. пока вы не можете выговорить слово "python" - начинать его учить не стоит
        ]
     )
    email = models.EmailField()
    group = models.ForeignKey("courses.Group", on_delete=models.SET_NULL, null=True)

    class Meta:
        abstract = True


class Teacher(Person):
    pass


class Student(Person):
    pass


class Category(AbstractName):
    name = models.CharField(max_length=255, unique=True)


class CourseManager(models.Manager):
    def get_queryset(self):
        queryset = super(CourseManager, self).get_queryset()
        return queryset.filter(teacher__isnull=False)


class Course(AbstractName):
    category = models.ForeignKey('courses.Category', on_delete=models.SET_NULL, null=True)
    teacher = models.ForeignKey('courses.Teacher', on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(blank=True)
    thesis = models.CharField(max_length=255)

    objects = CourseManager()  # так же убирает отображение из админки. Правила едины для всех :(
