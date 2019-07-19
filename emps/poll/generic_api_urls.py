from django.urls import path, include
from .generic_api_views import *
from rest_framework.routers import DefaultRouter, SimpleRouter

router = DefaultRouter()
router.register('poll', PollViewSet)


poll_list_view = PollViewSet.as_view({"get": "list", "post": "create"})

urlpatterns = [
    path('generic/poll/', PollListView.as_view()),
    path('generic/poll/<int:id>/', PollListView.as_view()),
    # or for looking up primary key
    # path('generic/poll/<int:pk>/', PollListView.as_view()),
    path('poll/', include(router.urls)),
    path('list/', poll_list_view),
]
