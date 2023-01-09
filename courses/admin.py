from django.contrib import admin
from courses import models
from django import forms


class CourseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        self.fields['thesis'].widget = forms.Textarea()

    class Meta:
        model = models.Course
        exclude = ('',)


class CourseAdminForm(admin.ModelAdmin):
    form = CourseForm


admin.site.register(models.Group)
admin.site.register(models.Student)
admin.site.register(models.Teacher)
admin.site.register(models.Category)
admin.site.register(models.Course, CourseAdminForm)
