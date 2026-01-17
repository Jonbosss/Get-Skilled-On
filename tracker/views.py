from django.shortcuts import render, redirect  # Add redirect
from .models import Profile
from .forms import ActivityForm  # Add this import
import math


def profile_view(request):
    profile = Profile.objects.get(user=request.user)

    # Logic for saving the form
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.user = request.user
            activity.save()
            return redirect('profile')
    else:
        form = ActivityForm()

    # Your existing progress math
    def get_prog(xp, lvl):
        next_lvl_xp = (lvl ** 2) * 100
        return min(int((xp / next_lvl_xp) * 100), 100)

    context = {
        'profile': profile,
        'form': form,  # Pass the form to the template
        'str_prog': get_prog(profile.str_xp, profile.strength),
        'int_prog': get_prog(profile.int_xp, profile.intelligence),
        'cha_prog': get_prog(profile.cha_xp, profile.charisma),
    }

    return render(request, 'tracker/profile.html', context)
