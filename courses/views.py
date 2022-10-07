from django.views.generic import TemplateView, ListView
from courses.models import Category, Course


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({'categories': Category.objects.all()})
        return context


class CategoryView(ListView):
    model = Course
    template_name = "index.html"
    paginate_by = 10  # вот это делает доп. запрос

    def get_queryset(self):
        queryset = super(CategoryView, self).get_queryset()
        return queryset.filter(category=self.kwargs['cat']).select_related('teacher')

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context.update({'categories': Category.objects.all()})
        return context
