from django.urls import path
from courses.views import CourseCreateView, IndexView, CourseDetailView, StudentCreateView, CategoryView, CourseUpdateView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('course/<int:pk>', CourseDetailView.as_view(), name='course_detail'),
    path('add_course/', CourseCreateView.as_view(), name='course_create'),
    path('add_student/', StudentCreateView.as_view(), name='student_create'),
    path('category/<str:category>/', CategoryView.as_view(), name='category'),
    path('course/update/<int:pk>', CourseUpdateView.as_view(), name='course_update'),

]
