from django import forms
from .models import Book
from author.models import Author

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'description', 'count', 'authors']
        
    authors = forms.ModelMultipleChoiceField(
        queryset=Author.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
        required=False
    )