from django import forms
from django.contrib.auth.models import User
from hobby.models import HobbyCat, HobbyItem


class HobbyItemForm(forms.ModelForm):

    class Meta:
        model = HobbyItem
        fields = ('__all__')
