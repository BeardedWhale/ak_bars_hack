"""
This module is for main logic of finding car and house prices
"""
from loan_estimator.Item import Car
from loan_estimator.constants import CRWL_API_KEY, ADS_API_KEY
from loan_estimator.utils import get_cars_candidates, get_price, car_from_json

class Finder():

    def __init__(self):
        self.car_apis = [CRWL_API_KEY, ADS_API_KEY]
        self.house_apis = []

    def find_car_price(self, car_params: dict):
        """
        Finds most similar cars and predicts price
        :param car: json str that we receive from server in server request
        :return:
        """
        car = car_from_json(params=car_params) # ВОТ НЕ ЗНАЮ РАБОТАЕТ ИЛИ НЕТ
        print("HERE")
        cars_candidates = get_cars_candidates(car, number_of_candidates=20) #ВОТ ЭТО РАБОТАЕТ
        print("HERE2")
        price = get_price(car, cars_candidates) #И ВОТ ЭТО РАБОТАЕТ
        # print("HERE3")
        # TODO make it not return function but send a response to server with found values
        return cars_candidates, int(price)


    # TODO include getting candidates from second api to get_cars_candidates