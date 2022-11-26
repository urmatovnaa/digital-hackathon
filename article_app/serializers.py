from rest_framework import serializers
from article_app.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'name', 'user_name', 'data', 'photo']


class ArticleDetailSerializer(serializers.ModelSerializer):
    user_photo = serializers.ImageField()

    class Meta:
        model = Article
        fields = ['id', 'name', 'user_photo', 'data', 'photo', 'description']

