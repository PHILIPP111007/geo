from rest_framework import serializers

from .models import IPv4Location


class IPv4LocationSerializer(serializers.ModelSerializer):
	class Meta:
		model = IPv4Location
		exclude = ('id', 'ip_first', 'ip_last', )
