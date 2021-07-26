import requests
import logging


class APIBridge:
    def __init__(self, url, token=None, payload=None):
        self.url = url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/json;charset=utf-8',
        }
        if token:
            self.headers.update({'Authorization': f'Token {token}'})
        self.payload = payload

    def get(self):
        try:
            response = requests.get(url=self.url, headers=self.headers)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as er:
            logging.error('Something went wrong!' + repr(er))

    def post(self):
        pass
