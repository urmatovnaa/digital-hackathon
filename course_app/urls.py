from django.urls import path
from course_app.views import CourseViewSet, CourseDetailViewSet

urlpatterns = [
    path('', CourseViewSet.as_view({'get': 'list'})),
    path('create/', CourseViewSet.as_view({'post': 'create'})),
    path('<int:pk>/', CourseDetailViewSet.as_view(
        {'get': 'retrieve'}
    ))
]
