from django.db.models import F
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from course_app.models import Course
from course_app.serializers import CourseSerializer, CourseDetailSerializer


# class CourseViewSet(ModelViewSet):
#     serializer_class = CourseSerializer
#     serializer_classes = {
#         'retrieve': CourseDetailSerializer,
#     }
#     filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
#     search_fields = ['name', 'overview', ]
#     ordering_fields = ['name']
#     filterset_fields = ['format',]
#
#     def get_serializer_class(self):
#         return self.serializer_classes.get(self.action, self.serializer_class)
#
#     def get_queryset(self):
#         return Course.objects.all().annotate(category_name=F('category__name'))


class CourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['data']
    filterset_fields = ['time_study', 'category']


class CourseDetailViewSet(ModelViewSet):
    serializer_class = CourseDetailSerializer
    # permission_classes = [IsAuthenticated, ]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['data']
    filterset_fields = ['time_study', 'category']

    def get_queryset(self):
        return Course.objects.all().annotate(category_name=F('category__name'))