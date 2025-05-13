from django.urls import path, include

urlpatterns = [
    path('', include("client_management.urls.creating")),
    path('', include("client_management.urls.getting")),
    path('', include("client_management.urls.deleting")),
]