from django import forms
from .models import Post
#from .forms import CreateForm

class CreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')