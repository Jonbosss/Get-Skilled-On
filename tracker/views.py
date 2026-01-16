from django.shortcuts import render
from .models import Profile


def profile_view(request):
    # This finds the stats for the person currently logged in
    profile = Profile.objects.get(user=request.user)

    # This sends those stats to the webpage template
    return render(request, 'tracker/profile.html', {'profile': profile})
