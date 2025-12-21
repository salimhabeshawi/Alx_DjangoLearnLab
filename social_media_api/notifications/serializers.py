from rest_framework import serializers
from .models import Notification
from django.contrib.auth import get_user_model

class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.ReadOnlyField(source='actor.username')
    target = serializers.StringRelatedField() # Or custom field to show title/content

    class Meta:
        model = Notification
        fields = ['id', 'actor', 'verb', 'target', 'timestamp', 'read']
