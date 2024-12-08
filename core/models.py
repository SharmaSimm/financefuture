from django.db import models
from django.contrib.auth.models import User

class FinancialHealth(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='core_financialhealth', null=True, blank=True)  # Added related_name
    income = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    expenses = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    savings = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    financial_goals = models.TextField(default="No goals provided yet")  # Can be a JSON or string to store goals info
    score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    goals = models.TextField(null=True, blank=True)
    def __str__(self):
        return f'{self.user.username} Financial Health'

    def calculate_score(self):
        # Calculate score based on financial data
        if self.income > 0:
            return (self.savings / self.income) * 100
        return 0.0

    def save(self, *args, **kwargs):
        self.score = self.calculate_score()  # Automatically calculate score before saving
        super().save(*args, **kwargs)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    def __str__(self):
        return f'{self.user.username} Profile'
