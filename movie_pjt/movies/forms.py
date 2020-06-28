from django import forms
from .models import Movie, Review, Comment

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'content']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class SearchForm(forms.ModelForm):
    word = forms.CharField(label='Search Word')