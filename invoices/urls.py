from rest_framework.routers import DefaultRouter
from .views import InvoiceViewSet, ClientViewSet, PaymentViewSet, ItemViewSet
from django.urls import path, include


router = DefaultRouter()
router.register(r'invoices', InvoiceViewSet, basename='invoice')
router.register(r'clients', ClientViewSet, basename='client')
router.register(r'payments', PaymentViewSet, basename='payment')
router.register(r'items', ItemViewSet, basename='item')


urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/register/', include('dj_rest_auth.registration.urls')),
]
urlpatterns += router.urls
