from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from .models import Post, Comment, Cookbook
from .forms import CommentForm
import random

# Create your views here.


# class PostList(generic.ListView):
# queryset = Post.objects.filter(status=1)
# template_name = "blog/index.html"
# paginate_by = 14


def PostList(request):

    page_number = request.GET.get('page', 1)
    paginator = Paginator(Post.objects.filter(status=1), 18)
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/index.html', {'page_obj': page_obj})


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


def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
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


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
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


def cookbook_contents(request, slug):
    cookbook = get_object_or_404(Cookbook, slug=slug)
    dishes = Cookbook.dishes.objects.all()
    context = { 'dishes': dishes, 'cookbook': cookbook, }
    return render(request, 'blog/cookbook_contents.html', context)


def cookbook_edit(request, slug, cookbook_id):
    if request.method == "POST":
        cookbook = get_object_or_404(Cookbook, slug=slug)
        cookbook_form = CookbookPostForm(data=request.POST, instance=cookbook)
        if cookbook_form.is_valid() and cookbook.collector == request.user:
            cookbook = cookbook_form.save(commit=False)
            cookbook.save()
            messages.add_message(request, messages.SUCCESS, 'Cookbook Updated!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating cookbook!')
    return HttpResponseRedirect(reverse('cookbook_content', args=[slug]))


def cookbook_delete(request, slug, cookbook_id):
    cookbook = get_object_or_404(Cookbook, pk=cookbook_id)
    if cookbook.collector == request.user:
        cookbook.delete()
        messages.add_message(request, messages.SUCCESS, 'Cookbook deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own cookbooks!')
    return HttpResponseRedirect(reverse('view_chefprofile', args=[slug]))