from rest_framework import serializers

from .models import IPv4Location, IPv6Location


class IPv4LocationSerializer(serializers.ModelSerializer):
	class Meta:
		model = IPv4Location
		exclude = ('id', 'ip_first', 'ip_last', )


class IPv6LocationSerializer(serializers.ModelSerializer):
	class Meta:
		model = IPv6Location
		exclude = ('id', 'ip_first', 'ip_last', )
