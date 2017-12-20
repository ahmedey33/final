from django import forms
from django.contrib.auth.models import User
from . models import Blog


class AddpostForm(forms.ModelForm):

	class Meta:
		model = Blog
		fields = ('__all__')

