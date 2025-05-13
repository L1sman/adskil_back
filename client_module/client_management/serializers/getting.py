from rest_framework import serializers
from client_management.models import Offer, PaymentTerm, Client


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'


class PaymentTermSerializer(serializers.ModelSerializer):
    start_date = serializers.DateField(format="%d.%m.%Y")

    class Meta:
        model = PaymentTerm
        fields = '__all__'


class ClientGetSerializer(serializers.ModelSerializer):
    start_date = serializers.DateField(format="%d.%m.%Y")
    offers = OfferSerializer(many=True, read_only=True)
    payment_terms = PaymentTermSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = '__all__'
