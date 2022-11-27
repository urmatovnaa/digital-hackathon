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
    people_count = RegisteredSerializer(read_only=True, many=True)
    speakers_detail = SpeakersSerializer(read_only=True, many=True)

    class Meta:
        model = Event
        fields = '__all__'
        extra_kwargs = {
            'user': {'read_only': True}
        }

    def to_representation(self, instance):
        response = super().to_representation(instance)
        print(response)
        response['last_seats'] = (response['number_for_seats']) - len(response['people_count'])
        print(response['last_seats'])
        return response
