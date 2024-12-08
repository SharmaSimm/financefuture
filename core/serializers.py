from rest_framework import serializers
from .models import UserProfile

from .models import FinancialHealth

class FinancialHealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialHealth
        fields = ['income', 'expenses', 'savings', 'financial_goals', 'score']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'income', 'expenses', 'savings_rate', 'debt']
