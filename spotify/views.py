import json
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .credentials import REDIRECT_URI, CLIENT_SECRET, CLIENT_ID
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from requests import Request, post
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .util import update_or_create_user_tokens, is_spotify_authenticated, get_user_tokens, execute_spotify_api_request
from .models import Playback
from .serializers import *
from users.models import User
from users.serializers import UserSerializer


class AuthURL(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        scopes = 'user-read-playback-state user-modify-playback-state user-read-currently-playing'

        url = Request('GET', 'https://accounts.spotify.com/authorize', params={
            'scope': scopes,
            'response_type': 'code',
            'redirect_uri': REDIRECT_URI,
            'client_id': CLIENT_ID,
            'state': self.request.user.id
        }).prepare().url

        return Response({'url': url}, status=status.HTTP_200_OK)


class spotify_callback(APIView):
    def get(self, request, format=None):
        code = request.GET.get('code')
        state = request.GET.get('state')
        error = request.GET.get('error')

        response = post('https://accounts.spotify.com/api/token', data={
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': REDIRECT_URI,
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET
        }).json()

        access_token = response.get('access_token')
        token_type = response.get('token_type')
        refresh_token = response.get('refresh_token')
        expires_in = response.get('expires_in')
        error = response.get('error')

        pk = update_or_create_user_tokens(
            state, access_token, token_type, expires_in, refresh_token)

        return redirect('http://localhost:3000/')


class SpotifyIsAuthenticated(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        is_authenticated = is_spotify_authenticated(self.request.user.id)
        return Response({'status': is_authenticated}, status=status.HTTP_200_OK)
    
class PlaybackInfo(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        endpoint = "player/currently-playing"
        response = execute_spotify_api_request(self.request.user.id, endpoint)

        if 'error' in response or 'item' not in response:
            return Response({}, status=status.HTTP_204_NO_CONTENT)

        item = response.get('item')
        duration = item.get('duration_ms')
        progress = response.get('progress_ms')
        album_cover = item.get('album').get('images')[0].get('url')
        is_playing = response.get('is_playing')
        song_id = item.get('id')

        artist_string = ""

        for i, artist in enumerate(item.get('artists')):
            if i > 0:
                artist_string += ", "
            name = artist.get('name')
            artist_string += name

        song = {
            'title': item.get('name'),
            'artist': artist_string,
            'duration': duration,
            'time': progress,
            'image_url': album_cover,
            'is_playing': is_playing,
            'votes': 0,
            'id': song_id
        }

        return Response(song, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        users = User.objects.all()
        endpoint = "player/currently-playing"

        for u in users:
            response = execute_spotify_api_request(u.id, endpoint)
            if 'item' not in response:
                print(u.email, 'isn\'t listening to anything.') 
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
                        print('Playback updated successfully.')
                except Playback.DoesNotExist:
                    playback_serializer = PlaybackSerializer(data={'user': u.id, 'title': response.get('item').get('name'), 'artists': artist_string})
                    if playback_serializer.is_valid():
                        playback_serializer.save()
                        print('Playback created successfully.')
            
        return Response(status=status.HTTP_200_OK)    
    