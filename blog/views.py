from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Post, Comment, Cookbook
from .forms import CommentForm
from chefprofile.forms import NewDishForm
from chefprofile.forms import NewCookbookForm
import random
from django.views.decorators.http import require_POST


def PostList(request):
    if request.user.is_authenticated:
        cookbooks = Cookbook.objects.filter(collector=request.user)
    else:
        cookbooks = Cookbook.objects.none()
    posts = Post.objects.filter(status=1).order_by('?')
    page_number = request.GET.get('page', 1)
    paginator = Paginator(posts, 18)
    page_obj = paginator.get_page(page_number)
    if request.method == 'POST':
        if 'save_to_cookbook' in request.POST:
            cookbook_id = request.POST.get('cookbook_id')
            cookbook = get_object_or_404(Cookbook, id=cookbook_id, collector=request.user)
            post_id = request.POST.get('save_to_cookbook')
            if post_id.isdigit():
                post_id = int(post_id)    
                cookbook.dishes.add(post_id)
                cookbook.save()
                messages.add_message(request, messages.SUCCESS, 'Recipe added to cookbook!')
                return redirect('home')
    return render(request, 'blog/index.html', {'page_obj': page_obj, 'cookbooks': cookbooks,})


@login_required
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    cookbooks = Cookbook.objects.filter(collector=request.user)
    comment_form = CommentForm()
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter().count()

    if request.method == 'POST':
        if 'post_comment' in request.POST:
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.author = request.user
                comment.post = post
                comment.save()
                messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval')
                return redirect('post_detail', slug=slug)
        elif 'save_to_cookbook' in request.POST:
            cookbook_id = request.POST.get('cookbook_id')
            cookbook = get_object_or_404(Cookbook, id=cookbook_id, collector=request.user)
            cookbook.dishes.add(post)
            cookbook.save()
            messages.add_message(request, messages.SUCCESS, 'Recipe added to cookbook!')
            return redirect('post_detail', slug=slug)
    context = {
        'post': post,
        'comment_form': comment_form,
        "comment_count": comment_count,
        "comments": comments,
        'cookbooks': cookbooks,
    }
    return render(request, 'blog/post_detail.html', context)


@login_required
def comment_edit(request, slug, comment_id):
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


@login_required
def comment_delete(request, slug, comment_id):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


@login_required
def cookbook_contents(request, slug):
    cookbook = get_object_or_404(Cookbook, slug=slug)
    dishes = cookbook.dishes.all()
    context = { 'dishes': dishes, 'cookbook': cookbook, }
    return render(request, 'blog/cookbook_contents.html', context)


@login_required
def edit_cookbook(request, slug):
    cookbook = get_object_or_404(Cookbook, slug=slug)
    if request.method == 'POST':
        cookbook_form = NewCookbookForm(
            request.POST, request.FILES, instance=cookbook)
        if cookbook_form.is_valid():
            cookbook = cookbook_form.save(commit=False)
            if 'cover_image' in request.FILES:
                cookbook.cover_image = request.FILES['cover_image']
            cookbook.save()
            messages.add_message(request, messages.SUCCESS, 'Cookbook Updated!')
            return redirect('view_chefprofile')
    else:
        cookbook_form = NewCookbookForm(instance=cookbook)
    return render(request, 'blog/edit_cookbook.html', {'cookbook_form': cookbook_form})


@login_required
def cookbook_delete(request, slug, cookbook_id):
    cookbook = get_object_or_404(Cookbook, pk=cookbook_id)
    if cookbook.collector == request.user:
        cookbook.delete()
        messages.add_message(request, messages.SUCCESS, 'Cookbook deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own cookbooks!')
    return HttpResponseRedirect(reverse('view_chefprofile'))


@require_POST
def remove_recipe_from_cookbook(request):
    post_id = request.POST.get('post_id')
    cookbook_slug = request.POST.get('cookbook_slug')
    cookbook = get_object_or_404(Cookbook, slug=cookbook_slug, collector=request.user)
    post = get_object_or_404(Post, id=post_id)
    cookbook.dishes.remove(post)
    dishes = cookbook.dishes.all()
    messages.add_message(request, messages.SUCCESS, 'Recipe removed from cookbook.')
    return render(request, 'blog/cookbook_contents.html', {'dishes': dishes, 'cookbook': cookbook})


@login_required
def edit_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        post_form = NewDishForm(
            request.POST, request.FILES, instance=post)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            if 'featured_image' in request.FILES:
                post.featured_image = request.FILES['featured_image']
            post.save()
            messages.add_message(request, messages.SUCCESS, 'Recipe Updated!')
            return redirect('view_chefprofile')
    else:
        post_form = NewDishForm(instance=post)
    return render(request, 'blog/edit_post.html', {'post_form': post_form})


@login_required
def post_delete(request, slug, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if post.author == request.user:
        post.delete()
        messages.add_message(request, messages.SUCCESS, 'Recipe deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own recipes!')
    return HttpResponseRedirect(reverse('view_chefprofile'))