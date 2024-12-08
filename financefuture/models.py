from django.db import models
from django.contrib.auth.models import User

class FinancialGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal_type = models.CharField(max_length=50)  # e.g., 'Saving', 'Debt Repayment'
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    progress = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    due_date = models.DateField()

    def __str__(self):
        return f'{self.user.username} - {self.goal_type} Goal'

class CommunityBenchmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)  # e.g., 'Income vs Expenses'
    value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.user.username} - Benchmark for {self.category}'

class FinancialHealth(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='financefuture_financialhealth', null=True, blank=True)  # Added related_name
    income = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    expenses = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    savings = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, null=True)
    financial_goals = models.TextField(default="No goals provided yet")  # Can be a JSON or string to store goals info
    score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    goals = models.TextField(null=True, blank=True)
    def __str__(self):
        return f"Financial Health for {self.user.username}"
    def calculate_score(self):
        # Calculate score based on financial data
        if self.income > 0:
            return (self.savings / self.income) * 100
        return 0.0

    def save(self, *args, **kwargs):
        self.score = self.calculate_score()  # Automatically calculate score before saving
        super().save(*args, **kwargs)
