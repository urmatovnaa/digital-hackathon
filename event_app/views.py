from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from event_app.models import Event, Registered, Category
from event_app.serializers import EventsSerializer, EventsDetailSerializer, \
    RegisteredSerializer, CategorySerializer
from question_app.permissions import IsAuthorPermission
    

class EventsViewSet(ModelViewSet):
    serializer_class = EventsSerializer
    queryset = Event.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['data']
    filterset_fields = ['category']
    permission_classes = (IsAuthorPermission,)


class EventsDetailViewSet(ModelViewSet):
    serializer_class = EventsDetailSerializer
    permission_classes = [IsAuthorPermission, ]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['data']
    filterset_fields = ['category']
    queryset = Event.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RegisteredViewSet(APIView):
    serializer_class = RegisteredSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Registered.objects.all()
    lookup_field = 'event_pk'

    def get(self, request, event_pk):
        created = Registered.objects.filter(event_id=event_pk, user=request.user).exists()
        if created:
            Registered.objects.filter(
                event_id=event_pk,
                user=request.user
            ).delete()

            return Response({'success': 'Отменить запись'})
        else:
            Registered.objects.create(event_id=event_pk, user=request.user)
            return Response({'success': 'Записаться'})


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['data']
    filterset_fields = ['category']
