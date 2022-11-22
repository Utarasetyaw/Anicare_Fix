from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
from accounts.models import DiscussConversation, DiscussTopic


class DiscussTopicSerializer(ModelSerializer):
    class Meta:
        model = DiscussTopic
        fields = ('id', 'id_author', 'title', 'description')

    def create(self, validated_data):
        discuss = DiscussTopic.objects.create(
            id_author = validated_data['id_author'],
            title   = validated_data['title'],
            description = validated_data['description']

        )
    
        return discuss


class DiscussConversationSerializer(ModelSerializer):
    class Meta:
        model = DiscussConversation
        fields = ('id', 'id_topic', 'id_author', 'text')
    
    def create(self, validated_data):
        discuss_convo = DiscussConversation.objects.create(
            id_topic = validated_data['id_topic'],
            id_author = validated_data['id_author'],
            text = validated_data['text']
        )
    
        return discuss_convo


