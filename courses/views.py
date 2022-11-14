from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, FormView, UpdateView, TemplateView
from courses.models import Course, Student, DelayedMail
from courses.forms import CourseCreateForm, StudentCreateForm


class IndexView(ListView):
    model = Course
    template_name = 'index.html'

    def get_queryset(self):
        return self.model.objects.select_related('teacher')


class StudentListView(ListView):
    model = Student
    template_name = 'students.html'

    def get_queryset(self):
        return self.model.objects.select_related('group')


class CategoryView(IndexView):
    paginate_by = 10

    def get_queryset(self):
        queryset = super(CategoryView, self).get_queryset()
        return queryset.filter(category=self.kwargs['category']).select_related('teacher')


class UserProfileTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'user_profile.html'
    form_class = ''


class CourseDetailView(DetailView):
    model = Course
    template_name = 'course_detail.html'


class StudentDetailView(DetailView):
    model = Student
    template_name = 'student_detail.html'


class CourseCreateView(CreateView):
    form_class = CourseCreateForm
    template_name = 'create.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context.update({'title': 'Add course'})
        return context

    def form_valid(self, form):
        course = form.save()
        form.send_email()
        DelayedMail(course=course, name=course.name).save()
        return super(CourseCreateView, self).form_valid(form)


class StudentCreateView(FormView):
    form_class = StudentCreateForm
    template_name = 'create.html'
    success_url = '/students'

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context.update({'title': 'Add student'})
        return context

    def form_valid(self, form):
        form.save()
        return super(StudentCreateView, self).form_valid(form)


class CourseUpdateView(UpdateView):
    model = Course
    template_name = "course_update.html"
    form_class = CourseCreateForm
    success_url = '/'


class StudentUpdateView(UpdateView):
    model = Student
    template_name = "student_update.html"
    form_class = StudentCreateForm
    success_url = '/students'
