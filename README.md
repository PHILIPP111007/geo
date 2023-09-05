# Geo

Get your geo location based on IP address or GPS.

## Usage

Go to `localhost:3000` and you will see minimalistic GUI with two buttons: get position by GPS and IP.

```json
// After getting `localhost:8000/api/ip/` you will see something lile that:

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

// or that:

{
    "ip": "2001:0db8:0a0b:12f0:0000:0000:0000:0001",
    "type": "IPv6",
    "info": {
        "continent": "ZZ",
        "country": "ZZ",
        "stateprov": "",
        "city": "",
        "latitude": 0.0,
        "longitude": 0.0
    }
}
```

```json
// After getting `localhost:8000/api/gps/` you will see this:

{
    "coords": {
        "accuracy": 10.2,
        "altitude": null,
        "altitudeAccuracy": null,
        "heading": null,
        "latitude": 38.7519,
        "longitude": -90.4409,
        "speed": null
    },
    "timestamp": 123123213
}
```

## Installation

This app works with `Postgres` (https://www.postgresql.org/), `PostGIS` (https://postgis.net/) and needs to be installed `gdal` (https://gdal.org/index.html) dependency.

First of all you need to run Postgres server. Then go to backend directory.
```sh
cd backend
```

Run `setup.sh` script to create venv, DB migrations, superuser and collect static files.
```sh
bash setup.sh
```

Activate python virtual enviroment.
```sh
source venv/bin/activate
```

Download data base (.csv) from https://db-ip.com/db/download/ip-to-city-lite (about 450 Mb) and run this script that will save it to Postgres DB (it will take about 10 minutes).
```sh
python manage.py shell < create_db.py
```

Run app server.
```sh
python manage.py runserver
```

Then go to the frontend directory.

```sh
cd ../frontend
```

Install npm packages.
```sh
npm install
```

Create production frontend app.
```sh
npm run build
```

Run the frontend app.
```sh
serve -s build
```

## Notes
* App uses a third-party free data base: https://db-ip.com/db/download/ip-to-city-lite.