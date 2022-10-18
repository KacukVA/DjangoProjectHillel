from django import forms
from django.core.exceptions import ValidationError
from courses.models import Student, Course


class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'teacher': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),
            'thesis': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),
        }


class StudentCreateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'group': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if first_name.count(' '):
            raise ValidationError("First name can not contain spaces")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if last_name.count(' '):
            raise ValidationError("Last name can not contain spaces")
        return last_name
