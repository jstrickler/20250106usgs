import requests
from requests import Response
import json
from typing import Any

# endpoint reference
# https://m2m.cr.usgs.gov/api/docs/reference/

EROS_URL = "https://m2m.cr.usgs.gov/api/api/json/stable/"

class EROSBase:
    def __init__(self, *, username: str, application_token: str):
        self._username: str = username
        self._application_token: str = application_token
        self._get_login_token()

    def _get_login_token(self):
        login_data: dict[str,str] = {"username": self._username, "token": self._application_token}
        response: Response = requests.post(EROS_URL + "login-token", data=json.dumps(login_data))
        if response.ok:
            self._login_token = response.json()['data']
        else:
            raise Exception("Unable to get API KEY")

    @property
    def username(self) -> str:
        return self._username
    
    @property
    def application_token(self) -> str:
        return self._application_token

    @property
    def login_token(self) -> str:
        return self._login_token

    def _get_data(self, *, endpoint: str, params: dict[str,str]) -> dict[str, Any]:
        headers =  {'X-Auth-Token': self._login_token}
        response: Response = requests.post(
            EROS_URL + endpoint, 
            data=json.dumps(params), 
            headers=headers
        )
        if response.ok:
            return response.json()['data']
        else:
            raise Exception("Unable to get API KEY")     

    def __del__(self):
        self._get_data(endpoint='logout', params={})
