from django.urls import path
from .api_views import *


urlpatterns = [
    path('poll/', PollAPIView.as_view()),
    path('poll/<int:id>/', PollDetailView.as_view()),
]
