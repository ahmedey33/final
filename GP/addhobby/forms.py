from django import forms
from django.contrib.auth.models import User
from hobby.models import HobbyCat


class HobbyForm(forms.ModelForm):

    class Meta:
        model = HobbyCat
        fields = ('__all__')


  		# fields = ('artist', 'album_title',)
  		# exclude = ['album_logo']

# class HobbyForm(forms.Form):
#     album_name = forms.CharField(label='HobbyCat Name', max_length=100)
#     (...)

# class UserForm(forms.ModelForm):
#     password = forms.CharField(widget = forms.PasswordInput)
#
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']
#
#
# class LoginForm(forms.ModelForm):
#     password = forms.CharField(widget = forms.PasswordInput)
#     class Meta:
#         model = User
#         fields = ['username', 'password']
