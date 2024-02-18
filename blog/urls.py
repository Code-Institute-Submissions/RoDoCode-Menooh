from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList, name='home'),
    path('posts/<slug:slug>/', views.post_detail, name='post_detail'),
    path('posts/<slug:slug>/edit_comment/<int:comment_id>',
        views.comment_edit, name='comment_edit'),
    path('posts/<slug:slug>/delete_comment/<int:comment_id>',
        views.comment_delete, name='comment_delete'),
    path('cookbooks/<slug:slug>/', views.cookbook_contents, name='cookbook_contents'),
    path('cookbooks/edit/<slug:slug>/', views.edit_cookbook, name='edit_cookbook'),
    path('cookbooks/<slug:slug>/delete_cookbook/<int:cookbook_id>',
        views.cookbook_delete, name='cookbook_delete'),
    path('cookbook/remove_recipe/', views.remove_recipe_from_cookbook, name='remove_recipe_from_cookbook'),
    path('posts/edit/<slug:slug>/', views.edit_post, name='edit_post'),
    path('posts/<slug:slug>/post_delete/<int:post_id>',
        views.post_delete, name='post_delete'),
]
