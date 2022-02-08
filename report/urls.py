from django.urls import path

from .views import ReportView, SuccessView

urlpatterns = [
    path("", ReportView.as_view(), name="report"),
    path("success/", SuccessView.as_view(), name="success"),
]
