from django import forms
 
from .models import Item

class FormItem(forms.ModelForm):
    class Meta:
            model=Item
            fields='__all__'