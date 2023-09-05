from django.contrib.gis.db import models


class IPv4Location(models.Model):
	ip_first = models.PositiveBigIntegerField() # First IP address in the block
	ip_last = models.PositiveBigIntegerField() # Last IP address in the block
	continent = models.CharField(max_length=2) # Two-letter continent code [AF, AS, EU, NA, OC, SA, AN]
	country = models.CharField(max_length=2) # ISO 3166-1 alpha-2 country code (2 letter)
	stateprov = models.TextField() # State or Province name
	city = models.TextField() # City name
	latitude = models.FloatField() # Decimal latitude
	longitude = models.FloatField() # Decimal longitude

	class Meta:
		verbose_name = 'IPv4 Location'
		ordering = ['ip_first']

	def __str__(self):
		return str(self.pk)


class IPv6Location(models.Model):
	ip_first = models.DecimalField(max_digits=100, decimal_places=0)
	ip_last = models.DecimalField(max_digits=100, decimal_places=0)
	continent = models.CharField(max_length=2)
	country = models.CharField(max_length=2)
	stateprov = models.TextField()
	city = models.TextField()
	latitude = models.FloatField()
	longitude = models.FloatField()

	class Meta:
		verbose_name = 'IPv6 Location'
		ordering = ['ip_first']

	def __str__(self):
		return str(self.pk)


class GPSLocation(models.Model):
	point = models.PointField(dim=2, srid=4326, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, null=True)

	class Meta:
		verbose_name = 'GPS Location'

	def __str__(self):
		return str(self.pk)
