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
from .tasks import *


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
    
class PlaybackList(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        playback_list = Playback.objects.all()
        playback_dict = {pb.user.id: {'title': pb.title, 'artists': pb.artists} for pb in playback_list}

        return Response(playback_dict, status=status.HTTP_200_OK)