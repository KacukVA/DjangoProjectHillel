from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from courses.views import CourseCreateView, IndexView, CourseDetailView, StudentCreateView, CategoryView, \
    CourseUpdateView, StudentListView, StudentDetailView, StudentUpdateView, UserProfileTemplateView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('students/', StudentListView.as_view(), name='students'),
    path('course/<int:pk>', CourseDetailView.as_view(), name='course_detail'),
    path('student/<int:pk>', StudentDetailView.as_view(), name='student_detail'),
    path('add_course/', CourseCreateView.as_view(), name='course_create'),
    path('add_student/', StudentCreateView.as_view(), name='student_create'),
    path('category/<str:category>/', CategoryView.as_view(), name='category'),
    path('course/update/<int:pk>', CourseUpdateView.as_view(), name='course_update'),
    path('student/update/<int:pk>', StudentUpdateView.as_view(), name='student_update'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', UserProfileTemplateView.as_view(), name='profile'),
]
