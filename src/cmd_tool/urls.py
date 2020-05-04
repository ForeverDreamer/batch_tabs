from django.urls import path

from .views import CollectstaticAPIView, MigrateAPIView

urlpatterns = [
    path('collectstatic/', CollectstaticAPIView.as_view(), name='collectstatic'),
    path('migrate/', MigrateAPIView.as_view(), name='migrate'),
]
