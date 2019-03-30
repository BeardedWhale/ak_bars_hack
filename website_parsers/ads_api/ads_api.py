import json
import time
from typing import List, Tuple
import requests
from Item import Car
from website_parsers.ads_api.constants import ADSResponseCode, REAL_ESTATE_CATEGORIES
from website_parsers.base_api import BaseApi
from datetime import datetime
from datetime import timedelta

SLEEP_TIME = 10  # 20 seconds between requests
import os

ACCESS_TOKEN = '6d743e61f3391fa046d3a2dbc763b038'


class ADS_API(BaseApi):

    def __init__(self):
        super().__init__('ads_api', sleep_time=SLEEP_TIME)
        self.access_token = ACCESS_TOKEN
        self.mail = 'lisch.batanina@icloud.com'
        self.last_request_time = datetime.now() - timedelta(seconds=10)

    def register_api(self):
        pass

    def send_auto_request(self, mark: str, model: str, engine: str = '', mileage: str = '',
                          gearbox: str = '', year: str = '', start_id: int = 0) -> Tuple[List[Car], int]:
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
        url = f'http://ads-api.ru/main/api?user={self.mail}&token={self.access_token}'
        q = f'{mark} {model}'
        if year:
            q += f' {year}г'
        if mileage:
            q += f' пробег {mileage}км'
        if engine:
            q += f' двигатель {engine}'
        if gearbox:
            q += f' {gearbox} КПП'

        url += f'&q={q}'
        if start_id:
            url += f'&startid={start_id}'

        response = requests.get(url)
        self.last_request_time = datetime.now()
        if response.status_code == ADSResponseCode.SUCCESS:
            response_body = response.text
            response_data = json.loads(response_body)
            cars_dict = response_data.get('data', [])
            if not cars_dict:
                return [], start_id
            num_cars = len(cars_dict)
            cars = [Car(self.name, car_dict) for car_dict in cars_dict]
            start_id = cars_dict[num_cars - 1]['id']
            return cars, start_id
        return [], start_id

    # def send_real_estate_request(self, category: str, region: str, area: int=0, start_id:int=0)->Tuple[List[Item], int]:
    #     """
    #     Sends request for real estate data to API
    #     :param category: real estate category ['Квартиры', 'Комнаты', 'Дома, дачи, коттеджи',
    #     'Коммерческая недвижимость', 'Недвижимость за рубежом']
    #     :param region: region of a real estate
    #     :param area: area of our hous
    #     :param start_id:  start id to retrieve adverts starting from this id
    #     :return: List[Category], start id
    #     """
    #     curr_time = datetime.now()
    #     time_diff = curr_time - self.last_request_time
    #     if time_diff > self.sleep_time:
    #         time.sleep(time_diff.seconds - self.sleep_time.seconds)
    #     url = f'http://ads-api.ru/main/api?user={self.mail}&token={self.access_token}'
    #     if category not in REAL_ESTATE_CATEGORIES.keys():
    #         return  [], start_id
    #     url += f'q={category} в {region}'
