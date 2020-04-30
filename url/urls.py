from django.urls import path

from .views import RestoreUrlsAPIView, BatchTabsAPIView

urlpatterns = [
    path('restore/', RestoreUrlsAPIView.as_view(), name='batch-tabs'),
    path('open/', BatchTabsAPIView.as_view(), name='batch-tabs'),
]
