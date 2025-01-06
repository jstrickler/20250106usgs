from pprint import pprint
import requests

URLS = {
    'datasets': (
        'https://www.ncdc.noaa.gov/cdo-web/api/v2/datasets',
        {}
    ),
    'stations': (
        'https://www.ncdc.noaa.gov/cdo-web/api/v2/stations',
        {'limit': 10, 'locationid': "FIPS:42"}
    ),
    'station_id': (
        'https://www.ncdc.noaa.gov/cdo-web/api/v2/stations/COOP:010957',
        {}
    ),
}

TOKEN = 'RZvAuJvzafAimtwbJFmORyXQbOpEoVId'

session = requests.Session()
session.headers.update({'token': TOKEN})

for url_name, (url, params) in URLS.items():
    print(f"**** {url_name.upper()} ****")
    response = session.get(
        url,
        params=params,
    )

    pprint(response.json())
    print('-' * 60)
