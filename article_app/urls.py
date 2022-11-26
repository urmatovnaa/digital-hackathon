from django.urls import path, include
from article_app.views import ArticleViewSet, ArticleDetailViewSet

urlpatterns = [
    path('', ArticleViewSet.as_view({'get': 'list'})),
    path('<int:pk>/', ArticleDetailViewSet.as_view(
        {'get': 'retrieve'}
    ))
]
