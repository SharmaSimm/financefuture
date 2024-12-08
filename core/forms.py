from django import forms
from .models import UserProfile, FinancialHealth

# Form for user profile
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture']

# Form for financial health questionnaire
class FinancialHealthForm(forms.ModelForm):
    class Meta:
        model = FinancialHealth
        fields = ['income', 'expenses', 'savings', 'goals']
