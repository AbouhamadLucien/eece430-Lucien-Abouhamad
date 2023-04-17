from django import forms
from .models import User
from .models import Coach

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'phone_number', 'email', 'gender', 'skill_level', 'password']
class CoachForm(forms.ModelForm):
    class Meta:
        model = Coach
        fields = ('username','first_name', 'last_name', 'phone_number', 'email', 'gender', 'password', 'experience', 'resume')

        