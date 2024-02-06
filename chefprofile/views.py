from django.shortcuts import render, redirect, get_object_or_404
from .models import ChefProfile
from .forms import ChefProfileForm


def edit_chefprofile(request):
    chefprofile = get_object_or_404(ChefProfile, user=request.user)

    if request.method == 'POST':
        chef_form = ChefProfileForm(data=request.POST, instance=chefprofile)
        if chef_form.is_valid():
            chef_form.save()
            messages.add_message(request, messages.SUCCESS, "Chef Profile \
                                 Updated")
            return redirect('chefprofile')

    else:
        chef_form = ChefProfileForm(instance=chefprofile)
        return render(request, 'chefprofile/edit_chefprofile.html', {'chef_form': chef_form})


def view_chefprofile(request):
    chefprofile = get_object_or_404(ChefProfile, user=request.user)
    context = {'chefprofile': chefprofile, }
    return render(request, 'chefprofile/view_chefprofile.html', context)
