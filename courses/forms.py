from django import forms
from django.core.exceptions import ValidationError
from courses.models import Student, Course, Category, Teacher, Group


class StudentCreateForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    group = forms.ModelChoiceField(queryset=Group.objects.all())
    age = forms.IntegerField(min_value=19, max_value=125)

    def create_student(self):
        student = Student.objects.create(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            group=self.cleaned_data['group'],
            age=self.cleaned_data['age'],
        )
        return student

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if first_name.count(' '):
            raise ValidationError("First name can not contain spaces")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if last_name.count(' '):
            raise ValidationError("Last name can not contain spaces")
        if Student.objects.filter(last_name=last_name).exists():
            raise ValidationError("Last name already exists")
        return last_name


class CourseCreateForm(forms.Form):
    name = forms.CharField()
    category = forms.ModelChoiceField(queryset=Category.objects.all(), to_field_name='name')
    teacher = forms.ModelChoiceField(queryset=Teacher.objects.all(), to_field_name='name')
    description = forms.CharField(required=False)
    thesis = forms.CharField(required=False)  # widget=forms.widgets.Textarea() - и без него все хорошо

    def create_course(self):
        course = Course.objects.create(
            name=self.cleaned_data['name'],
            category=self.cleaned_data['category'],
            teacher=self.cleaned_data['teacher'],
            description=self.cleaned_data['description'],
            thesis=self.cleaned_data['thesis']
        )
        return course

    def clean_name(self):
        name = self.cleaned_data['name']
        if Course.objects.filter(name=name.strip()).exists():
            raise ValidationError("Name already exists")
        return name
