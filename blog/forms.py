from .models import Comment, Cookbook
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class CookbookPostForm(forms.ModelForm):
    class Meta:
        model = Cookbook
        fields = ['dishes']
