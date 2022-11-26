from rest_framework import serializers

from question_app.models import Question, Answer


class AnswerSerializer(serializers.ModelSerializer):
    """Вывод ответа"""

    class Meta:
        model = Answer
        fields = '__all__'
        extra_kwargs = {
            'owner': {'read_only': True},
            'profile': {'read_only': True},
            'question': {'read_only': True},
        }


class QuestionSerializer(serializers.ModelSerializer):
    """Добавление вопроса"""
    answers_count = serializers.IntegerField(default=0, read_only=True)

    class Meta:
        model = Question
        fields = '__all__'
        extra_kwargs = {
            'owner': {'read_only': True},
            'profile': {'read_only': True},
        }


class QuestionDetailSerializer(serializers.ModelSerializer):
    """Детальный вопрос"""
    answers = AnswerSerializer(many=True)
    answers_count = serializers.IntegerField(default=0, read_only=True)

    class Meta:
        model = Question
        fields = '__all__'
        extra_kwargs = {
            'owner': {'read_only': True},
            'profile': {'read_only': True},
        }
