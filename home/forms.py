from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

class CommentForm(forms.ModelForm):
    text = forms.CharField(widget = forms.Textarea(
    attrs ={
        'placeholder':'Add your comment...',
        'rows':4,
        'cols':50
    }))

    class Meta:
        model = Comment
        fields = ["text"]
        labels = {
            "text": "Comment"
        }
        
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']