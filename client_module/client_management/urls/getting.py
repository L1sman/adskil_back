from django.urls import path
from client_management.views.getting import (
    ClientListView, ClientDetailView,
    ClientOffersView, ClientPaymentTermsView
)

urlpatterns = [
    path('clients/', ClientListView.as_view()),
    path('clients/<int:pk>/', ClientDetailView.as_view()),
    path('clients/<int:pk>/offers/', ClientOffersView.as_view()),
    path('clients/<int:pk>/payment_terms/', ClientPaymentTermsView.as_view()),
]
