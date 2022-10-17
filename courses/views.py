from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView, DetailView
from courses.models import Category, Course
from courses.forms import CourseCreateForm, StudentCreateForm


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({'categories': Category.objects.all()})
        return context


class CategoryView(ListView):
    model = Course
    template_name = "index.html"
    paginate_by = 4

    def get_queryset(self):
        queryset = super(CategoryView, self).get_queryset()
        return queryset.filter(category=self.kwargs['cat']).select_related('teacher')

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context.update({'categories': Category.objects.all()})
        return context


class CourseView(DetailView):
    template_name = 'index.html'


class CreateCourse(TemplateView):
    template_name = 'create_course.html'

    def get_context_data(self, **kwargs):
        context = super(CreateCourse, self).get_context_data(**kwargs)
        context['form'] = CourseCreateForm()
        return context

    def post(self, request):
        form = CourseCreateForm(data=request.POST)
        if form.is_valid():
            form.create_course()
            return redirect('/')

        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)


class CreateStudent(TemplateView):
    template_name = 'create_student.html'

    def get_context_data(self, **kwargs):
        context = super(CreateStudent, self).get_context_data(**kwargs)
        context['form'] = StudentCreateForm()
        return context

    def post(self, request):
        form = StudentCreateForm(data=request.POST)
        if form.is_valid():
            form.create_student()
            return redirect('/')

        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)
