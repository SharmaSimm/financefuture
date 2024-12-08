from rest_framework import serializers
from .models import FinancialHealth

class FinancialHealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialHealth
        fields = ['user_profile', 'score']
