from rest_framework import serializers
from .models import Playback

class PlaybackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playback
        fields = '__all__'