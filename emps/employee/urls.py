
from django.urls import path
from .views import *

urlpatterns = [
    path('employee_details/<int:id>', EmployeeDetail.as_view(),
         name='employee_details'),
    path('employee_add/', EmployeeAdd.as_view(), name='employee_add'),
    path('employee_update/<int:id>', EmployeeUpdate.as_view(),
         name='employee_update'),
]
