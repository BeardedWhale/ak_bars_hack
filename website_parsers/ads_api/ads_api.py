import json
import time
from typing import List
import requests
from Item import Car
from website_parsers.ads_api.constants import ADSResponseCode
from website_parsers.base_api import BaseApi
from datetime import datetime
from datetime import timedelta
SLEEP_TIME = 5 # 5 seconds between requests
import os
ACCESS_TOKEN = '6d743e61f3391fa046d3a2dbc763b038'


class ADS_API(BaseApi):

    def __init__(self):
        super().__init__('ads', sleep_time=SLEEP_TIME)
        self.access_token = ACCESS_TOKEN
        self.mail = 'lisch.batanina@icloud.com'
        self.last_request_time = datetime.now() - timedelta(seconds=10)

    def register_api(self):
        pass

    def send_auto_request(self, mark: str, model: str, engine: str='', mileage: str='',
                     gearbox: str='', year:str='', date_from:str='')->List[Car]:
        """
        Sends request
        :param mark: of automobile
        :param model: model of automobile
        :param engine: type of engine
        :param mileage: amount of kilometers passed
        :param gearbox: automative or not [механика, автомат, робот, вариатор]
        :param year: year of automobile
        :param date_from: start date of adverts
        :return: List of Car objects
        """
        curr_time = datetime.now()
        time_diff = curr_time - self.last_request_time
        if time_diff > self.sleep_time:
            time.sleep(time_diff.seconds - self.sleep_time.seconds)
        url = f'http://ads-api.ru/main/api?user={self.mail}&token={self.access_token}'
        q =f'{mark} {model}'
        if year:
            q += f' {year}г'
        if mileage:
            q += f' пробег {mileage}км'
        if engine:
            q += f' двигатель {engine}'
        if gearbox:
            q += f' {gearbox} КПП'

        url += f'&q={q}'
        if date_from:
            url += f'&date1={date_from}'

        response = requests.get(url)
        self.last_request_time = datetime.now()
        if response.status_code == ADSResponseCode.SUCCESS:
            response_body = response.text
            response_data = json.loads(response_body)
            cars_dict = response_data.get('data', [])
            # cars = [Car(car_dict) for car_dict in cars_dict]
            return cars_dict
        return []
