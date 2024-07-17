from django import forms
from .models import Blog, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'excerpt', 'body', 'author', 'date', 'photo']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
