from django import forms
from friendcard.models import FriendCard

class FriendlyForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

class CardCreateForm(forms.ModelForm):
    class Meta:
        model = FriendCard
        fields = ['name', 'author', 'created', 'nickname', 'gender', 'birthday', 'home', 'email', 'bio']
