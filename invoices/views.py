from .models import Invoice , Client, Payment, Item
from rest_framework.viewsets import ModelViewSet
from .serializer import InvoiceSerializer, ClientSerializer, PaymentSerializer, ItemSerializer
from django_filters.rest_framework import DjangoFilterBackend

class InvoiceViewSet(ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['client', 'status', 'due_date']
class ClientViewSet(ModelViewSet):
    model = Client
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

