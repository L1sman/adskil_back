from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from client_management.models import Client


class ClientDeleteView(APIView):
    def delete(self, request, pk):
        try:
            client = Client.objects.get(pk=pk)
            client.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Client.DoesNotExist:
            return Response({"detail": "Клиент не найден"}, status=status.HTTP_404_NOT_FOUND)
