from django.contrib import admin
# import your models here
from .models import Coin, Transaction, Country

# Register your models here
admin.site.register(Coin)
admin.site.register(Transaction)
admin.site.register(Country)
