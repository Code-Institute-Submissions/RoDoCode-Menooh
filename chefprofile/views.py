from django.shortcuts import render, redirect, get_object_or_404
from .models import ChefProfile
from .forms import ChefProfileForm
from django.contrib import messages


def edit_chefprofile(request):
    chefprofile = get_object_or_404(ChefProfile, user=request.user)

    if request.method == 'POST':
        chef_form = ChefProfileForm(request.POST, instance=chefprofile)
        if chef_form.is_valid():
            chef_form.save()
            messages.success(request, 'Profile updated successfully')
            return render(request, 'chefprofile/view_chefprofile.html', {'chefprofile': chefprofile, })
        else:
            messages.error(request,
                           ('Update failed. Please ensure '
                            'the form is valid.'))
            return render(request, 'chefprofile/edit_chefprofile.html', {'chef_form': chef_form})
    else:
        chef_form = ChefProfileForm(instance=chefprofile)
        return render(request, 'chefprofile/edit_chefprofile.html', {'chef_form': chef_form})


def view_chefprofile(request):
    chefprofile = get_object_or_404(ChefProfile, user=request.user)
    context = {'chefprofile': chefprofile, }
    return render(request, 'chefprofile/view_chefprofile.html', context)
