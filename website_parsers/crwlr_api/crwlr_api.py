import json
import time
from datetime import datetime, timedelta
from typing import Tuple, List

import requests

from Item import Car
from website_parsers.base_api import BaseApi
from constants import  CRWL_API_KEY
SLEEP_TIME = 0
ACCESS_TOKEN = '3a8eb204adac8c9cef297e691f921762'
class ADS_API(BaseApi):
    def __init__(self):
        super().__init__(CRWL_API_KEY, sleep_time=SLEEP_TIME)
        self.access_token = ACCESS_TOKEN
        self.mail = 'lisch.batanina@icloud.com'
        self.last_request_time = datetime.now() - timedelta(seconds=10)

    def send_auto_request(self, mark: str, model: str, engine: str='', mileage: str='',
                     gearbox: str='', year:str='', start_id:int=0)->Tuple[List[Car], int]:
        """
        Sends request for automobiles data to API
        :param mark: of automobile
        :param model: model of automobile
        :param engine: type of engine
        :param mileage: amount of kilometers passed
        :param gearbox: automative or not [механика, автомат, робот, вариатор]
        :param year: year of automobile
        :param start_id: start id to retrieve adverts starting from this id
        :return: List of Car objects
        """
        curr_time = datetime.now()
        time_diff = curr_time - self.last_request_time
        if time_diff < self.sleep_time:
            time.sleep(self.sleep_time.seconds - time_diff.seconds)
        url = f'http://crwl.ru/api/rest/latest/get_ads/?api_key={self.access_token}'

        response = requests.get(url)
        self.last_request_time = datetime.now()
        if response.status_code == 200:
            response_body = response.text
            response_data = json.loads(response_body)
            # TODO
            # cars_dict = response_data.get('data', [])
            if not cars_dict:
                return [], start_id
            num_cars = len(cars_dict)
            cars = [Car(self.name, car_dict) for car_dict in cars_dict]
            start_id = cars_dict[num_cars - 1]['id']
            return cars, start_id
        return [], start_id


