from pprint import pprint
import requests

BASE_URL = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/data'
TOKEN = 'RZvAuJvzafAimtwbJFmORyXQbOpEoVId'

session = requests.Session()
session.headers.update(
    {
        'token': TOKEN, 
        'UserAgent': "cja-tech.com,jstrickler@gmail.com", 
        'Accept': "application/GeoJSON"
    }
)

response = session.get(
    BASE_URL,
    params={
        'datasetid': 'PRECIP_HLY',
        'stationid': 'COOP:010957',
        'startdate': '1970-01-01',
        'enddate': '1970-12-31',
    },
    timeout=10,
)

pprint(response.json())
