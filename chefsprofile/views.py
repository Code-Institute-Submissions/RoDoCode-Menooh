from django.shortcuts import render, redirect
from .models import ChefsProfile
from .forms import ChefProfileForm


def edit_chefprofile(request):
    chefprofile = request.user.chefprofile

    if request.method == 'POST':
        form = ChefProfileForm(request.POST, instance=chefprofile)
        if form.is_valid():
            form.save()
            return redirect('chefprofile')
    else:
        form = ChefProfileForm(instance=chefprofile)

    return render(request, 'edit_chefprofile.html', {'form': form})


def view_chefprofile(request):
    return render(request, 'view_chefprofile.html')
