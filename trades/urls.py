from django.urls import path

from .views import TradeHistoryUploadView

urlpatterns = [
    path(r'uploads/', TradeHistoryUploadView.as_view(), name='uploads')
]
