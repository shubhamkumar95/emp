from django.urls import path, include
from .function_based_views import *
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('show_employee', EmployeeViewSet)

urlpatterns = [
    path('poll/', poll),
    path('poll/<int:id>/', poll_details),
]
