from django import forms
from django.contrib.auth.models import User
from betterforms.multiform import MultiModelForm
from accounts.models import Profile
from django.contrib.auth.forms import UserCreationForm
from accounts.widgets import DateInput

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nick', 'birth_date','aboutMe',]
        widgets = {
            'birth_date': DateInput()
        }

class UserCreationMultiForm(MultiModelForm):
    form_classes = {
        'user' : UserCreationForm,
        'profile' : ProfileForm,
    }
