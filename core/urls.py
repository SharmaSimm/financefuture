from django.urls import path
from . import views
from django.urls import path
from .views import FinancialHealthAPIView

urlpatterns = [
    # User profile page for viewing and updating profile data
    path('user-profile/', views.user_profile_view, name='user_profile'),

    # Financial health questionnaire page (for existing users to fill or update)
    path('financial-health/', views.financial_health_questionnaire, name='financial_health_questionnaire'),

    # Dashboard for viewing user progress and financial insights
    path('dashboard/', views.dashboard_view, name='dashboard'),

    # Financial health form page (new submission or editing, separate from the questionnaire)
    path('financial-health-form/', views.financial_health_view, name='financial_health'),

    path('api/financial-health/', FinancialHealthAPIView.as_view(), name='financial_health_api'),
]
