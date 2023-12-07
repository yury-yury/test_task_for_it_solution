from django.shortcuts import render
from django.db import models, transaction
from django.db.models import Count, Q, F
from rest_framework.viewsets import ModelViewSet

from my_app.models import User, Student, Course
from my_app.serializers import UserSerializer, StudentSerializer, CourseSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer

    def perform_destroy(self, instance: User):
        with transaction.atomic():
            instance.is_active = False
            instance.save(update_fields=('is_active', ))
            student = Student.objects.filter(user_id=instance.id).first()
            if student is not None:
                student.is_deleted = True
                student.save(update_fields=('is_deleted', ))


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.filter(is_deleted=False)
    serializer_class = StudentSerializer

    def list(self, request, *args, **kwargs):
        courses_name = request.GET.getlist('course', None)
        course_q = None
        for course in courses_name:
            if course_q is None:
                course_q = Q(courses__name__icontains=course)
            else:
                course_q |= Q(courses__name__icontains=course)

        if course_q:
            self.queryset = self.queryset.filter(course_q)

        return super().list(request, *args, **kwargs)



class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
