import uuid
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from chefprofile.models import ChefProfile


STATUS = ((0, "Draft"), (1, "Published"))


class Category(models.Model):
    title = models.CharField(max_length=250)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return f"{self.title}"


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    ingredients = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, verbose_name='Cuisine_Category')
    prep_time_minutes = models.PositiveIntegerField(default=25)
    prep_time_hours = models.PositiveIntegerField(default=0)
    cook_time_minutes = models.PositiveIntegerField(default=45)
    cook_time_hours = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"


class Cookbook(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    collector = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_cookbooks"
    )
    cover_image = CloudinaryField('image', default='placeholder')
    description = models.TextField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    dishes = models.ManyToManyField(Post, blank=True, related_name='books')

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | collected by {self.collector}"
