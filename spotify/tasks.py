from celery import shared_task
import time
from users.models import User
from users.serializers import UserSerializer
from .models import Playback
from .serializers import *
from .util import update_or_create_user_tokens, is_spotify_authenticated, get_user_tokens, execute_spotify_api_request


@shared_task
def update_playback():
    users = User.objects.all()
    endpoint = "player/currently-playing"

    for u in users:
            response = execute_spotify_api_request(u.id, endpoint)
            if 'item' not in response:
                print(u.email + ' isn\'t listening to anything.') 
            elif 'error' in response:
                error = response.get('error')
                print('Error getting user', u.id, '\'s playback info:', error)
            else:
                artist_string = ""
                for i, artist in enumerate(response.get('item').get('artists')):
                    if i > 0:
                        artist_string += ", "
                    name = artist.get('name')
                    artist_string += name

                try:
                    playback = Playback.objects.get(user=u.id)
                    playback_serializer = PlaybackSerializer(playback, data={'user': u.id, 'title': response.get('item').get('name'), 'artists': artist_string})
                    if playback_serializer.is_valid():
                        playback_serializer.save()
                        print(u.email + '\'s playback updated successfully.')
                except Playback.DoesNotExist:
                    playback_serializer = PlaybackSerializer(data={'user': u.id, 'title': response.get('item').get('name'), 'artists': artist_string})
                    if playback_serializer.is_valid():
                        playback_serializer.save()
                        print(u.email + '\'s playback created successfully.')
    
