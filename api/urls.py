from django.urls import include, path
from rest_framework import routers
from api import views
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register('students', views.StudentViewSet)
router.register('groups', views.GroupViewSet)
router.register('teachers', views.TeacherViewSet)

urlpatterns = [
    path('/', include(router.urls)),
    path('token/', obtain_auth_token),
]
