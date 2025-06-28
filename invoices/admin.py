from django.contrib import admin
from .models import Client, Invoice, Payment, Item
# Register your models here.
admin.site.register(Client)
admin.site.register(Invoice)
admin.site.register(Payment)
admin.site.register(Item)
