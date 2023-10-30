from django.urls import path
from . import views

urlpatterns = [
    path('get-auth-url', views.AuthURL.as_view()),
    path('redirect', views.SpotifyCallback.as_view()),
    path('is-authenticated', views.SpotifyIsAuthenticated.as_view()),
    path('playback', views.PlaybackList.as_view())
]