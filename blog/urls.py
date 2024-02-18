from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList, name='home'),
    path('posts/<slug:slug>/', views.post_detail, name='post_detail'),
    path('cookbooks/<slug:slug>/', views.cookbook_contents, name='cookbook_contents'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
]
