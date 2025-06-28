from rest_framework import serializers
from .models import Invoice, Client, Payment, Item

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class InvoiceSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    items = ItemSerializer(many=True, read_only=True)
    payments = PaymentSerializer(many=True, read_only=True)
    invoice_number = serializers.CharField(read_only=True, default=None)
    total_amount = serializers.SerializerMethodField()
    total_paid = serializers.SerializerMethodField()
    balance_due = serializers.SerializerMethodField()

    def get_total_amount(self, obj):
        return obj.total_amount
    def get_total_paid(self, obj):
        return obj.total_paid
    def get_balance_due(self, obj):
        return obj.balance_due
    
    class Meta:
        model = Invoice
        fields = '__all__'
        read_only_fields = ('total_amount', 'total_paid', 'balance_due')

