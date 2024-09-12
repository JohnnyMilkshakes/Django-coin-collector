from django.db import models

# A tuple of 2-tuples
TRANSACTION_TYPE = (
    ('B', 'Buy'),
    ('S', 'Sell'),
)

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=50)
    
    def __str__(self):
        return f"Name: {self.name}, Year: {self.year}, metal: {self.metal_type}"
    
# Create your models here.
class Coin(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField(max_length=100)
    metal_type = models.CharField()
    description = models.TextField(max_length=500)
    denomination = models.CharField(max_length=100)
    # country = models.ForeignKey()
    # owner = models.ForeignKey()
    
    def __str__(self):
        return f"Name: {self.name}, Year: {self.year}, metal: {self.metal_type}"
    
    
# Add new Feeding model below Cat model
class Transaction(models.Model):
  date = models.DateField('Transaction Date')
  type = models.CharField(
    max_length=1,
    # add the 'choices' field option
    choices=TRANSACTION_TYPE,
    # set the default value for transaction type to be 'B' or buy
    default=TRANSACTION_TYPE[0][0]
  )
  price = models.FloatField()
  # Create a coin_id FK
  coin = models.ForeignKey(Coin, on_delete=models.CASCADE)
  
  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.type} on {self.date}"

  # change the default sort
  class Meta:
    ordering = ['-date']
