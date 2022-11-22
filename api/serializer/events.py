from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
from accounts.models import Event


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'author', 'name', 'description', 'photo')

    def create(self, validated_data):

        event = Event.objects.create(
            **validated_data

        )
    
        return event