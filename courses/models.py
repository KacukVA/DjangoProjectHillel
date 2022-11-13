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
    course = models.ForeignKey("courses.Course", on_delete=models.CASCADE)
    # course = models.ForeignKey("courses.Course",  on_delete=models.SET_NULL, null=True)


class Person(AbstractName):
    age = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(125),
            MinValueValidator(18)
        ]
     )
    email = models.EmailField()
    group = models.ForeignKey("courses.Group", on_delete=models.SET_NULL, null=True)

    class Meta:
        abstract = True


class Teacher(Person):
    pass


class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, unique=True)
    group = models.ForeignKey("courses.Group", on_delete=models.SET_NULL, null=True)
    age = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(125),
            MinValueValidator(19)
        ]
     )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Category(AbstractName):
    name = models.CharField(max_length=255, unique=True)


class CourseManager(models.Manager):
    def get_queryset(self):
        queryset = super(CourseManager, self).get_queryset()
        return queryset.filter(teacher__isnull=False)


class Course(AbstractName):
    name = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey('courses.Category', on_delete=models.SET_NULL, null=True)
    teacher = models.ForeignKey('courses.Teacher', on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(blank=True)
    thesis = models.CharField(max_length=255, blank=True)

    objects = CourseManager()

    def __str__(self):
        return self.name
