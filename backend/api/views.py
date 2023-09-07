from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView

from .services import IPService, GPSService


class IPAPIView(APIView):

	def get(self, request: Request) -> Response:
		ip: str = IPService.get_client_ip(request=request)
		ip_obj = IPService.get_ip_obj(ip=ip)

		if not ip_obj:
			return Response({'ok': False, 'error': 'Invalid IP address.'}, \
				status=status.HTTP_404_NOT_FOUND)

		verbose_type = IPService.get_verbose_type_ip(ip=ip_obj)
		ip_info = IPService.find_ip_info(ip=ip_obj)

		if not ip_info:
			ip_info = 'No data.'

		resp = {
			'ok': True,
			'coords': {
				'ip': ip,
				'type': verbose_type,
				'info': ip_info
			}
		}
		return Response(resp, status=status.HTTP_200_OK)


class GPSAPIView(APIView):
	
	def post(self, request: Request) -> Response:
		result = GPSService.save_point(data=request.data)
		if result:
			return Response({'ok': True}, status=status.HTTP_200_OK)
		return Response({'ok': False}, status=status.HTTP_404_NOT_FOUND)
