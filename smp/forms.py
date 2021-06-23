from django import forms

from .models import *

class new_member(forms.ModelForm):
    class Meta:
        model = Member
        fields = [
            'Username',
            'Description',
            'Age',
            'Country',
            'Hobbies',
            'Question1',
            'Question2',
            'Question3'
        ]