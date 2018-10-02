from django import forms
from .models import User
import pdb

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'surname', 'age']