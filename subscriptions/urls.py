from django.urls import path

from .views import (
    SubscriptionListCreateView,
    SubscriptionDetailView,
)

urlpatterns = [
    path(
        '',
        SubscriptionListCreateView.as_view()
    ),

    path(
        '<int:pk>/',
        SubscriptionDetailView.as_view()
    ),
]