from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import ChefProfile
from blog.models import Post, Cookbook
from .forms import ChefProfileForm, NewDishForm, NewCookbookForm
from cloudinary.forms import cl_init_js_callbacks
from django.contrib import messages
from django.contrib.auth.models import User


@login_required
def edit_chefprofile(request):
    if request.method == 'POST':
        chef_form = ChefProfileForm(
            request.POST, request.FILES, instance=request.user.chefprofile)
        if chef_form.is_valid():
            chefprofile = chef_form.save(commit=False)
            if 'profile_pic' in request.FILES:
                chefprofile.profile_pic = request.FILES['profile_pic']
            chefprofile.save()
            return redirect('view_chefprofile')
    else:
        chef_form = ChefProfileForm(instance=request.user.chefprofile)
    return render(request, 'chefprofile/edit_chefprofile.html', {'chef_form': chef_form})


def view_chefprofile(request):
    chef_profile = ChefProfile.objects.get(user=request.user)
    chef_posts = Post.objects.filter(author=request.user)
    chef_cookbooks = Cookbook.objects.filter(collector=request.user)
    paginate_by = 20
    context = {
        'posts': chef_posts,
        'cookbooks': chef_cookbooks,
        'paginate_by': paginate_by,
    }
    return render(request, 'chefprofile/view_chefprofile.html', context)


@login_required
def new_dish(request):
    if request.method == 'POST':
        dish_form = NewDishForm(request.POST, request.FILES,)
        if dish_form.is_valid():
            Post = dish_form.save(commit=False)
            Post.author = request.user
            ugly_string = filter(str.isalnum, Post.title)
            clean_string = "".join(ugly_string)
            Post.slug = clean_string.casefold(
            )+str(request.user.pk)
            if 'featured_image' in request.FILES:
                Post.featured_image = request.FILES['featured_image']
            Post.save()
            messages.success(request, 'NEW DISH ADDED!')
            return redirect('view_chefprofile')
    else:
        dish_form = NewDishForm()
    return render(request, 'chefprofile/new_dish.html', {'dish_form': dish_form})


def new_cookbook(request):
    if request.method == 'POST':
        cookbook_form = NewCookbookForm(request.POST)
        if cookbook_form.is_valid():
            Cookbook = cookbook_form.save(commit=False)
            Cookbook.collector = request.user
            ugly_string = filter(str.isalnum, Cookbook.title)
            clean_string = "".join(ugly_string)
            Cookbook.slug = clean_string.casefold(
            )+str(request.user.pk)
            Cookbook.save()
            messages.success(request, 'NEW COOKBOOK ADDED!')
            return redirect('view_chefprofile')
        else:
            cookbook_form = NewDishForm()
    cookbook_form = NewCookbookForm()
    return render(request, 'chefprofile/new_cookbook.html', {'cookbook_form': cookbook_form})
