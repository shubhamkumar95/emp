from django.urls import path
from .generic_api_views import *


urlpatterns = [
    path('generic/poll/', PollListView.as_view()),
    path('generic/poll/<int:id>/', PollListView.as_view()),
    # or for looking up primary key
    # path('generic/poll/<int:pk>/', PollListView.as_view()),
]
