from django.urls import path
from .views import SMSIngestView

urlpatterns = [
    path('ingest/', SMSIngestView.as_view()),
]