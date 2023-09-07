from ipaddress import ip_address, IPv4Address, IPv6Address

from django.contrib.gis.geos import Point

from rest_framework.request import Request
from rest_framework.serializers import ReturnDict

from .models import IPv4Location, IPv6Location, GPSLocation
from .serializers import IPv4LocationSerializer, IPv6LocationSerializer


class IPService:

	@staticmethod
	def get_client_ip(request: Request) -> str:
		x_forwarded_for: str = request.META.get('HTTP_X_FORWARDED_FOR')
		ip: str = ''

		if x_forwarded_for:
			ip = x_forwarded_for.split(',')[0]
		else:
			ip = request.META.get('REMOTE_ADDR')

		return ip

	@staticmethod
	def get_ip_obj(ip: str) -> IPv4Address | IPv6Address | bool:
		try:
			ip_obj = ip_address(ip)
			return ip_obj
		except ValueError:
			return False

	@staticmethod
	def get_verbose_type_ip(ip: IPv4Address | IPv6Address) -> str:
		if isinstance(ip, IPv4Address):
			return 'IPv4'
		return 'IPv6'

	@staticmethod
	def find_ip_info(ip: IPv4Address | IPv6Address) -> ReturnDict | None:
		ip_int = int(ip)

		if isinstance(ip, IPv4Address):
			info = IPv4Location.objects \
				.filter(ip_first__lte=ip_int, ip_last__gte=ip_int)

			if info.exists():
				info = IPv4LocationSerializer(info[0]).data
			else:
				info = None
		else:
			info = IPv6Location.objects \
				.filter(ip_first__lte=ip_int, ip_last__gte=ip_int)

			if info.exists():
				info = IPv6LocationSerializer(info[0]).data
			else:
				info = None
		return info


class GPSService:

	@staticmethod
	def save_point(data: dict) -> bool:
		coords = data.get('coords', '')

		if coords:
			lat = coords.get('latitude')
			lon = coords.get('longitude')

			point = Point(x=lon, y=lat, srid=4326)
			GPSLocation.objects.create(point=point)

			return True
		return False
