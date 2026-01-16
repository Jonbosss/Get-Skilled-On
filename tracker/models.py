from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    strength = models.IntegerField(default=1)
    intelligence = models.IntegerField(default=1)
    charisma = models.IntegerField(default=1)
    str_xp = models.IntegerField(default=0)
    int_xp = models.IntegerField(default=0)
    cha_xp = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username}'s Stat Sheet"


class Activity(models.Model):
    CATEGORY_CHOICES = [
        ('STR', 'Strength'),
        ('INT', 'Intelligence'),
        ('CHA', 'Charisma'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)  # e.g., "Read 20 mins"
    category = models.CharField(max_length=3, choices=CATEGORY_CHOICES)
    xp_amount = models.IntegerField(default=10)  # How much XP this gives
    date_completed = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Activities"

    def __str__(self):
        return f"{self.title} (+{self.xp_amount} {self.category})"


@receiver(post_save, sender=Activity)
def update_user_stats(sender, instance, created, **kwargs):
    if created:
        # 1. Find the user's profile
        profile = Profile.objects.get(user=instance.user)

        # 2. Add XP based on the category
        if instance.category == 'STR':
            profile.str_xp += instance.xp_amount
        elif instance.category == 'INT':
            profile.int_xp += instance.xp_amount
        elif instance.category == 'CHA':
            profile.cha_xp += instance.xp_amount

        # 3. Save the updated profile
        profile.save()
