from django.urls import path, include
from event_app.views import EventsViewSet, EventsDetailViewSet, RegisteredViewSet

urlpatterns = [
    path('', EventsViewSet.as_view({'get': 'list'})),
    path('<int:pk>/', EventsDetailViewSet.as_view(
        {'get': 'retrieve'}
    )),
    path('<int:event_pk>/like/', RegisteredViewSet.as_view()),
]
