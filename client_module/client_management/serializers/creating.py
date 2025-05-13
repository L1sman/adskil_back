from rest_framework import serializers
from client_management.models import Offer, PaymentTerm, Client


class ClientCreateSerializer(serializers.ModelSerializer):
    start_date = serializers.DateField(format="%d.%m.%Y")

    def validate_name(self, value):
        if Client.objects.filter(name=value).exists():
            raise serializers.ValidationError("Клиент с таким именем уже существует.")
        return value

    class Meta:
        model = Client
        fields = '__all__'


class OfferCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Offer
        fields = '__all__'


class PaymentTermCreateSerializer(serializers.ModelSerializer):
    start_date = serializers.DateField(format="%d.%m.%Y")

    class Meta:
        model = PaymentTerm
        fields = '__all__'
