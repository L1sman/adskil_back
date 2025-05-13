from django.urls import path
from client_management.views.creating import ClientCreateView

urlpatterns = [
    path('clients/create/', ClientCreateView.as_view()),
]
