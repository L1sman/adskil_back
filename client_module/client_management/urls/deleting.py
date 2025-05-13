from django.urls import path
from client_management.views.deleting import ClientDeleteView

urlpatterns = [
    path('clients/<int:pk>/delete/', ClientDeleteView.as_view()),
]
