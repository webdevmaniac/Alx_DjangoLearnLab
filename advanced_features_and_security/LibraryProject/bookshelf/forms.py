from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'publication_year')

class ExampleForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    email = forms.EmailField(label='Your email', max_length=100)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Enter your name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your email'
