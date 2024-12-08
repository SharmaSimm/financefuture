"""
URL configuration for financefuture project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),  # This maps the root URL to the home view
    path('', include('core.urls')),  # Including the 'core' app URLs
    path('admin/', admin.site.urls),
    # Route for community benchmarking view
    path('community-benchmarking/', views.community_benchmarking, name='community_benchmarking'),

    # Route for financial goals page
    path('financial-goals/', views.financial_goals_view, name='financial_goals'),

    # Route for financial insights page
    path('financial-insights/', views.financial_insights_view, name='financial_insights'),



    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Main app URLs
    path('auth/', include('registration.urls')),  # Authentication URLs



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)