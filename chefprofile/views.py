from django.shortcuts import render, redirect, get_object_or_404
from .models import ChefProfile
from .forms import ChefProfileForm


def edit_chefprofile(request):
    chefprofile = get_object_or_404(ChefProfile, user=request.user)

    if request.method == 'POST':
        form = ChefProfileForm(request.POST, instance=chefprofile)
        if form.is_valid():
            form.save()
            return redirect('chefprofile')
    else:
        form = ChefProfileForm(instance=chefprofile)

    return render(request, 'edit_chefprofile.html', {'form': form})


def view_chefprofile(request):
    print('IN VIEW')
    print('USER: ', request.user)
    chefprofile = get_object_or_404(ChefProfile, user=request.user)
    print('PROFILE', chefprofile)
    context = {'chefprofile': chefprofile, }
    return render(request, 'view_chefprofile.html', context)
