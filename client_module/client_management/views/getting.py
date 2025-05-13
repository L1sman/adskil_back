from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from client_management.models import Client, Offer, PaymentTerm
from client_management.serializers.getting import ClientGetSerializer, OfferSerializer, PaymentTermSerializer
from django.shortcuts import get_object_or_404


class ClientListView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientGetSerializer


class ClientDetailView(generics.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientGetSerializer


class ClientOffersView(APIView):
    def get(self, request, pk):
        client = get_object_or_404(Client, pk=pk)
        offers = Offer.objects.filter(client=client)
        serializer = OfferSerializer(offers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ClientPaymentTermsView(APIView):
    def get(self, request, pk):
        client = get_object_or_404(Client, pk=pk)
        terms = PaymentTerm.objects.filter(client=client)
        serializer = PaymentTermSerializer(terms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
