from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator
from courses.models import Student, Course, Category, Teacher, Group


class StudentCreateForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    group = forms.ModelChoiceField(queryset=Group.objects.all(), to_field_name='name')
    age = forms.IntegerField()

    def create_student(self):
        product = Course.objects.create(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            group=self.cleaned_data['group'],
            age=self.cleaned_data['age'],
        )
        return product

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name'].strip()
        if ' ' in first_name:
            raise ValidationError("First name must not contain spaces")

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name'].strip()
        if ' ' in last_name:
            raise ValidationError("Last name must not contain spaces")
        if Student.objects.filter(last_name=last_name).exists():
            raise ValidationError("Last name already exists")
        return last_name

    def clean_age(self):
        age = int(self.cleaned_data['age'])
        if age < 18:
            raise ValidationError("Student must be older 18")


class CourseCreateForm(forms.Form):
    name = forms.CharField()
    category = forms.ModelChoiceField(queryset=Category.objects.all(), to_field_name='name')
    teacher = forms.ModelChoiceField(queryset=Teacher.objects.all(), to_field_name='name')
    description = forms.CharField(required=False)
    thesis = forms.CharField(required=False)  # widget=forms.widgets.Textarea() - и без него все хорошо

    def create_course(self):
        product = Course.objects.create(
            name=self.cleaned_data['name'],
            category=self.cleaned_data['category'],
            teacher=self.cleaned_data['teacher'],
            description=self.cleaned_data['description'],
            thesis=self.cleaned_data['thesis']
        )
        return product

    def clean_name(self):
        name = self.cleaned_data['name']
        if Course.objects.filter(name=name.strip()).exists():
            raise ValidationError("Name already exists")
        return name
