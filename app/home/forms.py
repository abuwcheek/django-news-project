from .models import New
from django import forms
from django.utils import  timezone

class NewCreateForm(forms.ModelForm):
    class Meta:
        model=New
        fields=["image", "title", "body", "category", "tags"]
        widgets={
            "title":forms.TextInput(attrs={'class':'form-control'}),
            "body":forms.Textarea(attrs={'class':'form-control'}),
            "category":forms.Select(attrs={'class':'form-control'}),
            "tags":forms.SelectMultiple(attrs={'class':'form-control'})

        }