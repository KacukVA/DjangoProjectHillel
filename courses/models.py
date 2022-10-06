from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class NameIt(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Group(NameIt):
    pass


class Person(NameIt):
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
