from django.urls import path
from .views import (
    TempDetailView
)
app_name = 'temps'
urlpatterns = [
    path('<int:id>/', TempDetailView.as_view(), name='temps_detail')
]