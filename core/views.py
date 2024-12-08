from django.shortcuts import render, redirect
from .models import UserProfile
from .forms import UserProfileForm, FinancialHealthForm
from financefuture.models import FinancialHealth
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FinancialHealth
from .serializers import FinancialHealthSerializer

# API for FinancialHealth
class FinancialHealthAPIView(APIView):
    def get(self, request):
        health = FinancialHealth.objects.filter(user=request.user).first()
        serializer = FinancialHealthSerializer(health)
        return Response(serializer.data)

    def post(self, request):
        serializer = FinancialHealthSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# View for the root URL
def home_view(request):
    return render(request, 'core/home.html')

# View to handle the user's profile page
@login_required
def user_profile_view(request):
    try:
        profile = UserProfile.objects.get(user=request.user)  # Retrieve the user's profile
    except UserProfile.DoesNotExist:
        profile = None  # If no profile exists, set to None

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()  # Save the form and update profile data
            return redirect('user_profile')  # Redirect to the same page after saving
    else:
        form = UserProfileForm(instance=profile)  # Show the existing profile form if no POST

    return render(request, 'core/user_profile.html', {'form': form, 'profile': profile})

# View to handle the financial health questionnaire
@login_required
def financial_health_questionnaire(request):
    # Check if the user already has financial health data
    try:
        financial_health = FinancialHealth.objects.get(user=request.user)
    except FinancialHealth.DoesNotExist:
        financial_health = None  # If no data exists, create an empty form

    if request.method == 'POST':
        form = FinancialHealthForm(request.POST, instance=financial_health)
        if form.is_valid():
            financial_health = form.save(commit=False)
            financial_health.user = request.user  # Link financial data to the current user
            financial_health.save()  # Automatically calculates score and saves

            return redirect('dashboard')  # Redirect to dashboard after submission
    else:
        form = FinancialHealthForm(instance=financial_health)  # Pre-fill the form if data exists

    return render(request, 'core/financial_health_questionnaire.html', {'form': form})

# View to display the user's financial insights and progress (Dashboard)
@login_required
def dashboard_view(request):
    # Retrieve the user's financial health data
    try:
        financial_health = FinancialHealth.objects.get(user=request.user)
    except FinancialHealth.DoesNotExist:
        financial_health = None  # If no data exists, set to None

    # Generate financial insights if data exists
    insights = {}
    score = None
    if financial_health:
        insights = generate_financial_insights(financial_health)
        score = calculate_financial_health_score(financial_health)

    return render(request, 'core/dashboard.html', {
        'financial_health': financial_health,
        'insights': insights,
        'score': score
    })

# Helper function to calculate the financial health score
def calculate_financial_health_score(financial_health):
    # Assume we are calculating the score based on income-to-savings ratio
    try:
        score = (financial_health.savings / financial_health.income) * 100
        return round(score, 2)
    except ZeroDivisionError:
        return 0  # Avoid division by zero if income is 0

# Helper function to generate financial insights
def generate_financial_insights(financial_health):
    # Generate insights based on financial data
    insights = {}
    if financial_health.income != 0:
        insights["income_to_expense_ratio"] = round((financial_health.income - financial_health.expenses) / financial_health.income * 100, 2)
    if financial_health.income != 0:
        insights["savings_percentage"] = round((financial_health.savings / financial_health.income) * 100, 2)

    return insights


@login_required
def financial_health_view(request):
    if request.method == 'POST':
        form = FinancialHealthForm(request.POST)
        if form.is_valid():
            financial_health = form.save(commit=False)
            financial_health.user = request.user
            financial_health.save()
            return redirect('dashboard')
    else:
        form = FinancialHealthForm()

    return render(request, 'core/financial_health_form.html', {'form': form})