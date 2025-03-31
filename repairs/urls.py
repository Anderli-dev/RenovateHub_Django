from django.urls import path
from repairs.views import HomeView, RepairRequestListView, MarkProcessedView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('requests/', RepairRequestListView.as_view(), name='request_list'),
    path('requests/<int:pk>/processed/', MarkProcessedView.as_view(), name='mark_processed'),
]
