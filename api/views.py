from rest_framework import viewsets
from api.serializer import StudentSerializer, GroupSerializer, TeacherSerializer
from courses import models


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = models.Student.objects.all()


class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = models.Group.objects.all()


class TeacherViewSet(viewsets.ModelViewSet):
    serializer_class = TeacherSerializer
    queryset = models.Teacher.objects.all()
