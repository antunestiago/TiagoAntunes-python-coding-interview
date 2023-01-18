from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from students.models import Student
from students.serializers import StudentSerializer


class StudentViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     GenericViewSet):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
