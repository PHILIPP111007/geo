from django.db import models


class IPv4Location(models.Model):

    # First IP address in the block
    ip_first = models.PositiveBigIntegerField()

    # Last IP address in the block
    ip_last = models.PositiveBigIntegerField()

    # continent
    # Two-letter continent code [AF, AS, EU, NA, OC, SA, AN]
    continent = models.CharField(max_length=2)

    # country
    # ISO 3166-1 alpha-2 country code (2 letter)
    country = models.CharField(max_length=2)

    # stateprov
    # State or Province name
    stateprov = models.CharField(max_length=50)

    # city
    # City name
    city = models.CharField(max_length=50)

    # latitude
    # Decimal latitude
    latitude = models.FloatField()
    
    # longitude
    # Decimal longitude
    longitude = models.FloatField()


    class Meta:
        verbose_name = 'IPv4 Location'
        ordering = ['ip_first', 'ip_last']
    
    def __str__(self):
        return self.pk


class IPv6Location(models.Model):

    # First IP address in the block
    ip_first = models.CharField(max_length=200)

    # Last IP address in the block
    ip_last = models.CharField(max_length=200)

    # continent
    # Two-letter continent code [AF, AS, EU, NA, OC, SA, AN]
    continent = models.CharField(max_length=2)

    # country
    # ISO 3166-1 alpha-2 country code (2 letter)
    country = models.CharField(max_length=2)

    # stateprov
    # State or Province name
    stateprov = models.CharField(max_length=50)

    # city
    # City name
    city = models.CharField(max_length=50)

    # latitude
    # Decimal latitude
    latitude = models.FloatField()
    
    # longitude
    # Decimal longitude
    longitude = models.FloatField()


    class Meta:
        verbose_name = 'IPv6 Location'
    
    def __str__(self):
        return self.pk
