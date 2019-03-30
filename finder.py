"""
This module is for main logic of finding car and house prices
"""
from Item import Car
from constants import CRWL_API_KEY, ADS_API_KEY
from utils import get_cars_candidates, get_price, car_from_json


class Finder():

    def __init__(self):
        self.car_apis = [CRWL_API_KEY, ADS_API_KEY]
        self.house_apis = []

    def find_car_price(self, car_str: str)->int:
        """
        Finds most similar cars and predicts price
        :param car: json str that we receive from server in server request
        :return:
        """
        car = car_from_json(js=car_str)
        cars_candidates = get_cars_candidates(car, number_of_candidates=20)
        price = get_price(car, cars_candidates)
        # TODO make it not return function but send a response to server with found values
        return cars_candidates, price


    # TODO include getting candidates from second api to get_cars_candidates