from django.db import models

class User(models.Model):
    username = models.CharField("Name", max_length=240)
    password = models.CharField(max_length=240)
    registrationDate = models.DateField("Registration Date", auto_now_add=True)

    def __str__(self) -> str:
        return self.username
