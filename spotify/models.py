from django.db import models
from users.models import User


class SpotifyToken(models.Model):
    user = models.IntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    refresh_token = models.CharField(max_length=300)
    access_token = models.CharField(max_length=300)
    expires_in = models.DateTimeField()
    token_type = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'User + {str(self.user)} + \'s token'
    
class Playback(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    artists = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.title} by {self.artists}'
    