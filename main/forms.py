from django import forms
from .models import CompInv

class PostForm(forms.ModelForm):

    class Meta:
        model = CompInv
        fields = ('comp_name', 'user_name',)