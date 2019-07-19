from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('show_employee', EmployeeViewSet)

urlpatterns = [
    path('show_employee/', include(router.urls)),
]
