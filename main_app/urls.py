from django.urls import path
from .views import Home, CoinList, CoinDetail # additional imports

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('coins/', CoinList.as_view(), name='coin-list'),
    path('coins/<int:id>/', CoinDetail.as_view(), name='coin-detail'),
]