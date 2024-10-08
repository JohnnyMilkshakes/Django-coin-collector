from django.urls import path
from .views import Home, CoinList, CoinDetail, TransactionListCreate, TransactionDetail, CountryList, CountryDetail # additional imports

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('coins/', CoinList.as_view(), name='coin-list'),
    path('coins/<int:id>/', CoinDetail.as_view(), name='coin-detail'),
    
    path('coins/<int:coin_id>/transactions/', TransactionListCreate.as_view(), name='transaction-list-create'),
	path('coins/<int:coin_id>/transactions/<int:id>/', TransactionDetail.as_view(), name='transaction-detail'),
 
    path('countries/', CountryList.as_view(), name='country-list'),
    path('countries/<int:id>/', CountryDetail.as_view(), name='country-detail'),
]