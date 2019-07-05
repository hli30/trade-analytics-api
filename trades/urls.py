from django.urls import path

from .views import TradeHistoryUploadView, TradeHistoryListView

urlpatterns = [
    path(r'uploads/', TradeHistoryUploadView.as_view(), name='uploads'),
    path(r'', TradeHistoryListView.as_view(), name='trade-history')
]
