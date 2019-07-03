from django.db import models
from django.conf import settings

class History(models.Model):
	EQUITY = 'EQ'
	ASSET_TYPE_CHOICES = [
		(EQUITY, 'Equity')
	]

	BUY = 'B'
	SELL = 'S'
	ACTION_CHOICES = [
		(BUY, 'Buy'),
		(SELL, 'Sell')
	]

	user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

	asset_type = models.CharField(max_length=2, choices=ASSET_TYPE_CHOICES)
	symbol = models.CharField(max_length=10)
	description = models.CharField(max_length=100, blank=True)
	action = models.CharField(max_length=1, choices=ACTION_CHOICES)
	quantity = models.IntegerField()
	price = models.DecimalField(max_digits=10 ,decimal_places=2)
	commission = models.DecimalField(max_digits=6 ,decimal_places=2)






