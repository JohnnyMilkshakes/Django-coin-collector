from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Coin
from .serializers import CoinSerializer

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