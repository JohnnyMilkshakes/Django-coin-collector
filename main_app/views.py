from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Coin, Transaction
from .serializers import CoinSerializer, TransactionSerializer

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
    transaction_id = self.kwargs['transaction_id']
    return Transaction.objects.filter(transaction_id=transaction_id)

  def perform_create(self, serializer):
    transaction_id = self.kwargs['transaction_id']
    transaction = Transaction.objects.get(id=transaction_id)
    serializer.save(transaction=transaction)
    
class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = TransactionSerializer
  lookup_field = 'id'

  def get_queryset(self):
    transaction_id = self.kwargs['transaction_id']
    return Transaction.objects.filter(transaction_id=transaction_id)