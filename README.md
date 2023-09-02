# Geo

Get your geo location based on IP address.

### Usage

After getting `YOUR_HOST/api/geo/` you will see something lile that:

```json
{
    "ip": "12.0.0.0",
    "type": "IPv4",
    "info": {
        "continent": "NA",
        "country": "US",
        "stateprov": "Missouri",
        "city": "Bridgeton",
        "latitude": 38.7519,
        "longitude": -90.4409
    }
}
```

### Installation

Run `setup.sh` script to create venv, DB migrations, superuser and collect static files.
```sh
bash setup.sh
```

Activate python virtual enviroment.
```sh
source venv/bin/activate
```

Download data base (it will take about 10 minutes).
```sh
python manage.py shell < create_db.py
```

Run app server.
```sh
python manage.py runserver
```

### Notes
* App uses a third-party free data base: https://db-ip.com/db/download/ip-to-city-lite.
* IPv6 is not supported in the app yet because SQLite does not work with long long integers.