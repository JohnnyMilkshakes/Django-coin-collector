from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Coin, Transaction, Country
from .serializers import CoinSerializer, TransactionSerializer, CountrySerializer

# Define the home view
class Home(APIView):
  def get(self, request):
    content = {'message': 'Welcome to the coin-collector api home route!'}
    return Response(content)

class CoinList(generics.ListCreateAPIView):
  queryset = Coin.objects.all()
  serializer_class = CoinSerializer

class CoinDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Coin.objects.all()
  serializer_class = CoinSerializer
  lookup_field = 'id'
  
class TransactionListCreate(generics.ListCreateAPIView):
  serializer_class = TransactionSerializer

  def get_queryset(self):
    coin_id = self.kwargs['coin_id']
    return Transaction.objects.filter(coin_id=coin_id)

  def perform_create(self, serializer):
    coin_id = self.kwargs['coin_id']
    coin = Transaction.objects.get(id=coin_id)
    serializer.save(coin=coin)
    
class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = TransactionSerializer
  lookup_field = 'id'

  def get_queryset(self):
    coin_id = self.kwargs['coin_id']
    return Transaction.objects.filter(coin_id=coin_id)

class CountryList(generics.ListCreateAPIView):
  queryset = Country.objects.all()
  serializer_class = CountrySerializer
    
class CountryDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Country.objects.all()
  serializer_class = CountrySerializer
  lookup_field = 'id'