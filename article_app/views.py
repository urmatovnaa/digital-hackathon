from django.db.models import F
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from article_app.models import Article
from article_app.serializers import ArticleSerializer, ArticleDetailSerializer


class ArticleViewSet(ModelViewSet):
    serializer_class = ArticleSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['data']
    filterset_fields = ['category']

    def get_queryset(self):
        queryset = Article.objects.annotate(
            user_name=F('user__fullname'),
        ).order_by('-id')
        return queryset


class ArticleDetailViewSet(ModelViewSet):
    serializer_class = ArticleDetailSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['data']
    filterset_fields = ['category']

    def get_queryset(self):
        queryset = Article.objects.annotate(
            user_photo=F('user__profile_image'),
        ).order_by('-id')
        return queryset

