from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm


def edit_profile(request):
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'edit_profile.html', {'form': form})


def view_profile(request):
    return render(request, 'view_profile.html')