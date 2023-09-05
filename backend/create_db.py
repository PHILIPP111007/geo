##########################################
# To run this file inside django execute:
# python manage.py shell < create_db.py
#
# At the bottom of this file specify the correct db path.
#
# Run this file only once.
##########################################
import os
import csv
import ipaddress

from api.models import IPv4Location, IPv6Location


def create_db(path):
	records_IPv4 = []
	records_IPv6 = []

	# Sample row for the IP to City Lite CSV file:
	# 8.8.8.0,8.8.8.255,NA,US,California,"Mountain View",37.4229,-122.085
	print('Cycle: Started.')
	
	with open(path, 'r') as file:
		reader = csv.reader(file)
		for line in reader:
			# DB.csv contains ipv4 and ipv6
			if len(line[0].split('.')) == 4:
				### Create content
				ip_first = ipaddress.IPv4Address(line[0])
				ip_last = ipaddress.IPv4Address(line[1])
				
				ip_first = int(ip_first)
				ip_last = int(ip_last)

				continent = line[2]
				country = line[3]
				stateprov = line[4]
				city = line[5]
				
				latitude = float(line[6])
				longitude = float(line[7])

				### Save record
				records_IPv4.append(
					IPv4Location(
						ip_first=ip_first,
						ip_last=ip_last,

						continent=continent,
						country=country,
						stateprov=stateprov,
						city=city,
								
						latitude=latitude,
						longitude=longitude,
					)
				)
			else:
				### Create content
				ip_first = ipaddress.IPv6Address(line[0])
				ip_last = ipaddress.IPv6Address(line[1])
				
				ip_first = int(ip_first)
				ip_last = int(ip_last)

				continent = line[2]
				country = line[3]
				stateprov = line[4]
				city = line[5]
				
				latitude = float(line[6])
				longitude = float(line[7])

				### Save record
				records_IPv6.append(
					IPv6Location(
						ip_first=ip_first,
						ip_last=ip_last,

						continent=continent,
						country=country,
						stateprov=stateprov,
						city=city,
								
						latitude=latitude,
						longitude=longitude,
					)
				)

	print(f'{len(records_IPv4) = }, {len(records_IPv6) = }')
	print('Cycle: Done.')

	### Create records
	print('DB: Started IPv4.')
	IPv4Location.objects.bulk_create(records_IPv4)
	print('DB: Done.')

	print('DB: Started IPv6.')
	IPv6Location.objects.bulk_create(records_IPv6)
	print('DB: Done.')


# File contains 5_581_382 records
# Downloaded from:
# https://db-ip.com/db/download/ip-to-city-lite
#
# Make sure that you have specified the correct db path:
db_csv_path: str = '/dbip-city-lite-2023-09.csv'


# Run from shell
if __name__ == 'django.core.management.commands.shell':
	if os.path.exists(db_csv_path):
		create_db(path=db_csv_path)
	else:
		print('ERROR: specify the correct DB path.')
