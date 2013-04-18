from django.forms import ModelForm
from admin.models import User
from admin.models import Role
from django.forms import Textarea
__author__ = 'jlchen'
from django import forms


class UserForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(required=False)
    description = forms.CharField()

    # def clean_name(self):
    #     name = self.cleaned_data['name']
    #     num_words = len(name.split())
    #     if num_words < 4:
    #         raise forms.ValidationError("Not enough words!")
    #     return name
class RoleForm(ModelForm):

    class Meta:
        model=Role
        fields=('name','description')
