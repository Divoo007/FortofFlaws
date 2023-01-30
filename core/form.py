from django import forms
from django.forms import ModelForm
from core.models import SignUp


class SignUpForm(ModelForm):
    class Meta:
        model = SignUp
        fields = ['name','email','password',]
    