from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        widgets = {'blog': forms.HiddenInput(), 'reviewer': forms.HiddenInput()}