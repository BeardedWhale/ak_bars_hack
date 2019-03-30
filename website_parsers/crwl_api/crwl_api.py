import datetime
import json
import time
import requests

from Item import Car
from website_parsers.base_api import BaseApi
from website_parsers.crwl_api.constants import CRWLResponseCode, REGIONS, REAL_ESTATE_CATEGORIES

SLEEP_TIME = 10  # 20 seconds between requests
ACCESS_TOKEN = 'c0bf868677c449f44b7c98cab00b77e4'


class CRWL_API(BaseApi):
    def __init__(self):
        super().__init__('crwl_api', sleep_time=SLEEP_TIME)
        self.access_token = ACCESS_TOKEN
        self.mail = 'lisch.batanina@icloud.com'
        self.last_request_time = datetime.datetime.now() - datetime.timedelta(seconds=10)

    def register_api(self):
        pass

    def send_auto_request(self, mark: str = '', model: str = ''):
        """

        :param mark:
        :param model:
        :return: list of Car objects
        """
        curr_time = datetime.datetime.now()
        time_diff = curr_time - self.last_request_time
        if time_diff < self.sleep_time:
            time.sleep(self.sleep_time.seconds - time_diff.seconds)
        if mark and model:
            url = f'http://crwl.ru/api/rest/latest/get_ads/?api_key={ACCESS_TOKEN}&brand={mark}&model={model}'
        else:
            url = f'http://crwl.ru/api/rest/latest/get_ads/?api_key={ACCESS_TOKEN}'
        response = requests.get(url)
        if response.status_code == CRWLResponseCode.SUCCESS:
            response_body = response.text
            response_data = json.loads(response_body)
            return [Car(self.name, car) for car in response_data]
        return []

    def send_house_request(self, category, region, ):
        """

        :return:
        """
        type_ad = 'продам'
        url = 'http://crwl.ru/api/rest/real-estate/latest/get_ads/?' \
              'api_key=c0bf868677c449f44b7c98cab00b77e4'
        region_id = REGIONS.get(region, '')
        if region_id:
            url += f'&region={region_id}'
        category_id = REAL_ESTATE_CATEGORIES.get(category, '')
        if category_id:
            url += f'&type={category_id}'
        url += f'&type_ad={type_ad}'
        print(url)
        response = requests.get(url)
        if response.status_code == CRWLResponseCode.SUCCESS:
            response_body = response.text
            response_data = json.loads(response_body)
            return response_data
        return  None
