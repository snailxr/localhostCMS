# coding=utf-8
from django.forms import ModelForm
from admin.models import User
from admin.models import Role
from django.forms import Textarea
__author__ = 'jlchen'
from django import forms


# class UserForm(forms.Form):
#     name = forms.CharField(widget=forms.TextInput(attrs={'class':'name'}))
#     email = forms.EmailField(required=False)
#     description = forms.CharField()
#     status=forms.CharField(
#                            widget=forms.Select(choices=User.USER_STATUS_CHOICES))
#     def clean_name(self):
#         name = self.cleaned_data['name']
#         num_words = len(name)
#         if num_words < 4:
#             raise forms.ValidationError("最少輸入4个字符!")
#         return name
class UserForm(ModelForm):
    class Meta:
        model=User
        fields=('name','email','description','status',)
        widgets={
            'name':forms.TextInput(attrs={'class':'name'}),
            'status':forms.Select(choices=User.USER_STATUS_CHOICES)
        }
    def clean_name(self):
        name = self.cleaned_data['name']
        num_words = len(name)
        if num_words < 4:
            raise forms.ValidationError("最少輸入4个字符!")
        return name
class RoleForm(ModelForm):
    class Meta:
        model=Role
        fields=('name','description',)
        widgets = {
            'name':forms.TextInput(attrs={'class':'name'})
            }
    def clean_name(self):
        name = self.cleaned_data['name']
        num_words = len(name)
        if num_words < 4:
            raise forms.ValidationError("最少輸入4个字符!")
        return name
