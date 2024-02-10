from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import ChefProfile
from blog.models import Post
from .forms import ChefProfileForm, NewDishForm
from django.contrib import messages
from django.contrib.auth.models import User


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


class view_chefprofile(generic.ListView):
    queryset = Post.objects.filter()
    template_name = "chefprofile/view_chefprofile.html"
    paginate_by = 20

"""
def new_dish(request):
    new_dish = get_object_or_404(Post, author=request.user)

    if request.method == 'POST':
        dish_form = NewDishForm(data=request.POST)
        if dish_form.is_valid():
            dish_form.save()
            messages.success(request, 'NEW DISH ADDED!')
            return HttpResponseRedirect(request, 'chefprofile/view_chefprofile.html')
        else:
            messages.error(request,
                           ('Dish creation failed. Please ensure '
                            'the form is valid.'))
            return render(request, 'chefprofile/new_dish.html', {'dish_form': dish_form})
    else:
        dish_form = NewDishForm(instance=new_dish)
        return render(request, 'chefprofile/new_dish.html', {'dish_form': dish_form})
"""


def new_dish(request):
    if request.method == 'POST':
        dish_form = NewDishForm(request.POST)
        if dish_form.is_valid():
            Post = dish_form.save(commit=False)
            Post.author = request.user
            Post.slug = Post.title.replace(" ", "").isalpha()
            Post.save()
            messages.success(request, 'NEW DISH ADDED!')
            return redirect('view_chefprofile')
        else:
            dish_form = NewDishForm()
    dish_form = NewDishForm()
    return render(request, 'chefprofile/new_dish.html', {'dish_form': dish_form})
