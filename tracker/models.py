from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):  # <--- Check this spelling
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    strength = models.IntegerField(default=1)
    intelligence = models.IntegerField(default=1)
    charisma = models.IntegerField(default=1)
    str_xp = models.IntegerField(default=0)
    int_xp = models.IntegerField(default=0)
    cha_xp = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username}'s Stat Sheet"
