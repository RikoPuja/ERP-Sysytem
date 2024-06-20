"""
URL configuration for erp_crm_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from crm.views import CustomerViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('finance/', include('finance.urls')),
    path('hrm/', include('hrm.urls')),
    path('inventory/', include('inventory.urls')),
    path('production/', include('production.urls')),
    path('project_management/', include('project_management.urls')),
    path('contacts/', include('contacts.urls')),
    path('sales/', include('sales.urls')),
    path('marketing/', include('marketing.urls')),
    path('customer_service/', include('customer_service.urls')),
    path('analytics/', include('analytics.urls')),
]
