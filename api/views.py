from ipaddress import ip_address, IPv4Address, IPv6Address

from django.db import models
from django.db.models.functions import Cast

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import IPv4Location, IPv6Location
from .serializers import IPv4LocationSerializer


def _get_client_ip(request) -> str:
	x_forwarded_for: str = request.META.get('HTTP_X_FORWARDED_FOR')
	ip: str = ''

	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[0]
	else:
		ip = request.META.get('REMOTE_ADDR')

	return ip


def _get_ip_obj(ip: str) -> IPv4Address | IPv6Address | bool:
	try:
		ip_obj = ip_address(ip)
		return ip_obj
	except ValueError:
		return False


def _get_verbose_type_ip(ip: IPv4Address | IPv6Address) -> str:
	if isinstance(ip, IPv4Address):
		return 'IPv4'
	return 'IPv6'


# TODO: create if-else based on the ip version
def _find_ip_info(ip: IPv4Address | IPv6Address) -> \
	models.QuerySet[IPv4Location] | models.QuerySet[IPv6Location]:

	ip_integer = int(ip)

	if isinstance(ip, IPv4Address):
		info = IPv4Location.objects \
			.filter(ip_first__lte=ip_integer, ip_last__gte=ip_integer)
	else:

		# ! OverflowError: Python int too large to convert to SQLite INTEGER
		# SQLite does not work with long long int

		# info = IPv6Location.objects \
		# 	.annotate(ip_first_integer=Cast('ip_first', output_field=models.IntegerField())) \
		# 	.annotate(ip_last_integer=Cast('ip_last', output_field=models.IntegerField())) \
		# 		.filter(ip_first_integer__lte=ip_integer, ip_last_integer__gte=ip_integer)
		
		# print(info.query)

		info = None # !

	return info


class GeoAPIView(APIView):
	serializer_class = IPv4LocationSerializer

	def get(self, request) -> Response:
		ip: str = _get_client_ip(request=request)

		# ip = '2001:4:111:ffff:ffff:ffff:ffff:ffff'
		ip = '12.0.0.0'	
		ip_obj = _get_ip_obj(ip=ip)

		if not ip_obj:
			return Response({'error': 'Invalid IP address.'}, status=status.HTTP_404_NOT_FOUND)

		verbose_type = _get_verbose_type_ip(ip=ip_obj)
		ip_info = _find_ip_info(ip=ip_obj)

		if ip_info:
			ip_info = IPv4LocationSerializer(ip_info[0]).data
		else:
			ip_info = 'No data.'

		resp = {
			'ip': ip,
			'type': verbose_type,
			'info': ip_info
		}

		return Response(resp, status=status.HTTP_200_OK)
