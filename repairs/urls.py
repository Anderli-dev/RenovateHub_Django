from django.urls import path
from repairs.views import HomeView, AdminHomeView, MarkProcessedView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('admin-panel/', AdminHomeView.as_view(), name='admin_home'),
    path('requests/<int:pk>/processed/', MarkProcessedView.as_view(), name='mark_processed'),
]
