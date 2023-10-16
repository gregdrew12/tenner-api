from django.db import models


class SpotifyToken(models.Model):
    user = models.IntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    refresh_token = models.CharField(max_length=200)
    access_token = models.CharField(max_length=200)
    expires_in = models.DateTimeField()
    token_type = models.CharField(max_length=50)

    def __str__(self) -> str:
        return 'User ' + str(self.user) + '\'s token'
    