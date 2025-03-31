from django.urls import path
from repairs.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]
