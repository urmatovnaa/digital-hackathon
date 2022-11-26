from django.urls import path
from question_app.views import QuestionViewSet, AnswerViewSet


urlpatterns = [
    path('', QuestionViewSet.as_view({'get': 'list'})),
    path('create/', QuestionViewSet.as_view({'post': 'create'})),
    path('<int:pk>', QuestionViewSet.as_view({'get': 'retrieve'})),
    path('<int:question_pk>/answer/', AnswerViewSet.as_view({'post': 'create'})),
]
