from rest_framework import serializers
from event_app.models import Category, Speaker, Event, Registered


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class SpeakersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Speaker
        fields = '__all__'


class RegisteredSerializer(serializers.ModelSerializer):

    class Meta:
        model = Registered
        fields = '__all__'


class EventsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ['id', 'name', 'photo', 'data']


class EventsDetailSerializer(serializers.ModelSerializer):
    counting = serializers.IntegerField()
    speakers_detail = SpeakersSerializer(many=True)

    class Meta:
        model = Event
        fields = ['id', 'name', 'data', 'photo', 'category', 'time', 'description', 'about',
                  'speakers_detail',
                  'user', 'number_for_seats', 'counting']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['last_seats'] = (response['number_for_seats']) - (response['counting'])
        people = response['speakers_detail']
        users = self.context['view'].request.user.id
        if users in people:
            response['Записаться'] = True
        return response
