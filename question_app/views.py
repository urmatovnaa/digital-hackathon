from django.db.models import Count
from rest_framework import status
from rest_framework.response import Response

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from question_app.serializers import QuestionSerializer, AnswerSerializer, QuestionDetailSerializer
from question_app.models import Question, Answer
from question_app.permissions import IsAuthorPermission


class QuestionViewSet(viewsets.ModelViewSet):
    """ Добавление вопроса"""
    serializer_class = QuestionSerializer
    permission_classes = (IsAuthorPermission,)
    serializer_classes = {
        'retrieve': QuestionDetailSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)

    def get_queryset(self):
        return Question.objects.all().annotate(answers_count=Count('answers'))


class AnswerViewSet(viewsets.ModelViewSet):
    """ Вывод вопрос и ответа"""
    serializer_class = AnswerSerializer
    permission_classes = (IsAuthorPermission,)
    lookup_field = 'question_pk'
    queryset = Answer.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(
            question_id=kwargs.get('question_pk')
        )
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers)

