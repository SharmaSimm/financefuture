from django.shortcuts import render
from .models import FinancialGoal, CommunityBenchmark
from core.models import FinancialHealth
from django.contrib.auth.decorators import login_required

# View to show the community benchmarking data
@login_required
def community_benchmarking(request):
    # Fetch relevant community benchmarking data
    benchmarks = CommunityBenchmark.objects.all()  # You can filter based on categories
    return render(request, 'financefuture/community_benchmarking.html', {'benchmarks': benchmarks})

# View to show user's financial goals
@login_required
def financial_goals_view(request):
    goals = FinancialGoal.objects.filter(user=request.user)
    return render(request, 'financefuture/financial_goals.html', {'goals': goals})

# View to show insights based on financial health
@login_required
def financial_insights_view(request):
    try:
        financial_health = FinancialHealth.objects.get(user=request.user)
    except FinancialHealth.DoesNotExist:
        financial_health = None

    insights = {}
    if financial_health:
        insights = generate_financial_insights(financial_health)

    return render(request, 'financefuture/financial_insights.html', {'insights': insights})

# Helper function for financial insights (can be customized)
def generate_financial_insights(financial_health):
    insights = {
        "income_to_expense_ratio": (financial_health.income - financial_health.expenses) / financial_health.income * 100,
        "savings_percentage": (financial_health.savings / financial_health.income) * 100
    }
    return insights
def home_view(request):
    # Your logic for the home page view
    return render(request, 'home.html')