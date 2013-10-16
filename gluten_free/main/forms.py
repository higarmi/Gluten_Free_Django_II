#encoding:utf-8 
from django.forms import ModelForm
from django import forms
from main.models import Recipe, Comments

class contactForm(forms.Form):
	email = forms.EmailField(label='Your Email address')
	message = forms.CharField(widget=forms.Textarea)

class recipeForm(ModelForm):
    class Meta:
        model = Recipe

class commentForm(ModelForm):
    class Meta:
        model = Comments
