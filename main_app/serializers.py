from rest_framework import serializers
from .models import Coin, Transaction

class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coin
        fields = '__all__'
        
class TransactionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Transaction
    fields = '__all__'
    read_only_fields = ('coin',)
