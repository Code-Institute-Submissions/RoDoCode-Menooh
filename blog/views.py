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
    queryset = Post.objects.filter()
    post = get_object_or_404(Post, slug=slug)
    cookbooks = Cookbook.objects.filter(collector=request.user)
    comment_form = CommentForm()
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

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
            return redirect('blog/post_detail', slug=slug)
    context = {
        'post': post,
        'comment_form': comment_form,
        "comment_count": comment_count,
        "comments": comments,
        'cookbooks': cookbooks,
    }
    return render(request, 'blog/post_detail.html', context)

"""
def post_detail(request, slug):

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()
    print('ID: ', post.id)
    return render(
        request,
        "blog/post_detail.html",
        {"post": post,
         "comments": comments,
         "comment_count": comment_count,
         "comment_form": comment_form, },
    )
"""

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
    queryset = Cookbook.dishes.objects.filter(status=1)
    cookbook = get_object_or_404(queryset, slug=slug)
