from django import forms
from django.utils import timezone

from .models import Comment, Post, User


class PostForm(forms.ModelForm):
    pub_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        initial=timezone.now(),
        label='Дата публикации'
    )

    class Meta:
        model = Post
        fields = (
            'title', 'text', 'image',
            'pub_date',
            'location', 'category')


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)
