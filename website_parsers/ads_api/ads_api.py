from website_parsers.base_api import BaseApi
SLEEP_TIME = 5 # 5 seconds between requests
import os
ACCESS_TOKEN = '6d743e61f3391fa046d3a2dbc763b038'


class ADS_API(BaseApi):

    def __init__(self):
        super().__init__('ads', sleep_time=SLEEP_TIME)
        self.access_token = ACCESS_TOKEN

    def register_api(self):
        pass

    def send_request(self):
        url = f'http://ads-api.ru/main/api?user=user@localhost.net&token={self.}'
