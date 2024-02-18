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
    path('cookbooks/<slug:slug>/edit_cookbook/<int:cookbook_id>',
         views.cookbook_edit, name='cookbook_edit'),
    path('cookbooks/<slug:slug>/delete_cookbook/<int:cookbook_id>',
         views.cookbook_delete, name='cookbook_delete'),
]
