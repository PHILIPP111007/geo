from django.contrib.gis.db import models


class IPv4Location(models.Model):
	ip_first = models.DecimalField(max_digits=13, decimal_places=0, \
		verbose_name='first IP address in the block')
	ip_last = models.DecimalField(max_digits=13, decimal_places=0, \
		verbose_name='fast IP address in the block')
	continent = models.CharField(max_length=2, \
		verbose_name='two-letter continent code [AF, AS, EU, NA, OC, SA, AN]')
	country = models.CharField(max_length=2, \
		verbose_name='ISO 3166-1 alpha-2 country code (2 letter)')
	stateprov = models.TextField(verbose_name='state or province name')
	city = models.TextField(verbose_name='city name')
	latitude = models.FloatField()
	longitude = models.FloatField()

	class Meta:
		verbose_name = 'IPv4 Location'
		ordering = ['ip_first']

	def __str__(self):
		return str(self.pk)


class IPv6Location(models.Model):
	ip_first = models.DecimalField(max_digits=39, decimal_places=0, \
		verbose_name='first IP address in the block')
	ip_last = models.DecimalField(max_digits=39, decimal_places=0, \
		verbose_name='last IP address in the block')
	continent = models.CharField(max_length=2, \
		verbose_name='two-letter continent code [AF, AS, EU, NA, OC, SA, AN]')
	country = models.CharField(max_length=2, \
		verbose_name='ISO 3166-1 alpha-2 country code (2 letter)')
	stateprov = models.TextField(verbose_name='state or province name')
	city = models.TextField(verbose_name='city name')
	latitude = models.FloatField()
	longitude = models.FloatField()

	class Meta:
		verbose_name = 'IPv6 Location'
		ordering = ['ip_first']

	def __str__(self):
		return str(self.pk)


class GPSLocation(models.Model):
	point = models.PointField(dim=2, srid=4326, null=True, \
		verbose_name='geo position point')
	timestamp = models.DateTimeField(auto_now_add=True, null=True)

	class Meta:
		verbose_name = 'GPS Location'

	def __str__(self):
		return str(self.pk)
