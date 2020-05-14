from django import forms
from basicapp.models import UserPortfolioModel
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta():
        model = User
        fields = ('username','password','email')

class UserPortfolioForm(forms.ModelForm):
    class Meta():
        model = UserPortfolioModel
        fields = ('portfolio_site','profile_pic')
