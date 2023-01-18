from rest_framework import serializers
from students.models import Student


class StudentSerializer(serializers.ModelSerializer):
    enrollment = serializers.SerializerMethodField(method_name='check_subjects')

    @staticmethod
    def check_subjects(instance):
        if len(instance.subjects.all()) >= 7:
            instance.enrollment = True

    class Meta:
        model = Student
        fields = '__all__'
