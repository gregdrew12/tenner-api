from django.urls import path
from . import views

urlpatterns = [
    path('get-auth-url', views.AuthURL.as_view()),
    path('redirect', views.spotify_callback.as_view()),
    path('is-authenticated', views.SpotifyIsAuthenticated.as_view()),
    path('playback', views.PlaybackInfo.as_view())
]