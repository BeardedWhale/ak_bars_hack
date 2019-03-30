import datetime
import json
import re
from typing import List
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor

from Item import Car
from constants import *
from website_parsers.ads_api.ads_api import ADS_API
from website_parsers.crwl_api.crwl_api import CRWL_API

ads_api = ADS_API()
crwl_api = CRWL_API()
apis = [ads_api, crwl_api]


def params_match(car, estimated_car):
    """ марка, год, модель, двигатель, пробег, год, статус(битая?),
        тип кузова, КПП, руль, мощность двигателя(лс) """
    # assert(car.brand == estimated_car.brand)
    # assert(car.model == estimated_car.model)=
    car_engine_type = car.engine_type.replace(' ', '')
    if car.brand.lower() != estimated_car.brand.lower():
        return False
    if car.model.lower() != estimated_car.model.lower():
        return False
    # # Engine type match: gasoline, diesel ...
    # if estimated_car.engine_type:
    #     if car_engine_type != estimated_car.engine_type:
    #         return False
    #
    # # Engine volume difference in range
    # if estimated_car.engine_volume:
    #     if abs(car.engine_volume - estimated_car.engine_volume) > max_engine_vol_diff:
    #         return False
    #
    # # Year of production doesn't differ much
    # if estimated_car.year:
    #     if abs(car.year - estimated_car.year) > max_year_diff:
    #         return False
    #
    # # Kilometers run difference
    # if estimated_car.km:
    #     if abs(car.km - estimated_car.km) > max_km_diff:
    #         return False
    #
    # # Cars have same transmission
    # if estimated_car.kpp:
    #     if car.kpp != estimated_car.kpp:
    #         return False
    #
    # # Horse power doesn't differ much
    # if estimated_car.engine_horse_power:
    #     if abs(car.engine_horse_power - estimated_car.engine_horse_power) > max_engine_hp_diff:
    #         return False

    return True


def filter(cars, estimated_car):
    """ Check list of cars to match required filters """
    matched_cars = []
    for car in cars:
        if params_match(car, estimated_car):
            matched_cars.append(car)
    return matched_cars


def estimate_car(estimated_car: Car, number_of_candidates=10):
    """

    :param estimated_car:
    :return:
    """
    # global ads_api
    retrieved_cars = []
    start_id = 0
    filtered = []
    tried_once_more = False

    while not len(retrieved_cars) >= number_of_candidates:

        cars1, last_id = ads_api.send_auto_request(estimated_car.brand, estimated_car.model, start_id=start_id)
        cars2, _ = crwl_api.send_auto_request(estimated_car.brand, estimated_car.model, start_id=start_id)
        print(cars1)
        print(cars2)
        cars = merge_cars_lists(cars1, cars2)
        print(len(retrieved_cars))
        print(len(cars))
        if start_id and cars:
            if tried_once_more:
                cars.pop(0)  # remove first element as we already retrieved it
            elif len(cars) == 1:
                tried_once_more = True
        if not cars:
            break
        filtered = filter(cars, estimated_car)

        retrieved_cars.extend(filtered)
        start_id = last_id
    return retrieved_cars


def merge_cars_lists(cars1, cars2):
    result = cars1
    urls = [car.url for car in cars1]
    if not len(cars2) and len(cars1): return cars1
    if not len(cars1) and len(cars2): return cars2
    for car in cars2:
        if car.url not in urls:
            urls.append(car.url)
            result.append(car)
    return result


def car_similarity_score(car, other_car) -> int:
    score = 0
    if car.brand == other_car.brand:
        score += 0.2
    if car.model == other_car.model:
        score += 0.2
    if car.engine_type == other_car.engine_type:
        score += 0.15
    if car.kpp == other_car.kpp:
        score += 0.15

    if isinstance(car.engine_volume, int) and isinstance(other_car.engine_volume, int):
        score -= 0.07 * abs(car.engine_volume - other_car.engine_volume)
    if isinstance(car.engine_horse_power, int) and isinstance(other_car.engine_horse_power, int):
        score -= 0.07 * abs(car.engine_horse_power - other_car.engine_horse_power)
    if isinstance(car.year, int) and isinstance(other_car.year, int):
        score -= 0.07 * abs(car.year - other_car.year)
    return score


def get_cars_candidates(car: Car, number_of_candidates: int) -> List[Car]:
    """
    This method finds most similar cars to a query car
    :param car: Car
    :param number_of_candidates: amount of similar cars to find
    :return: list of cars
    """

    number_of_retreived_cars = number_of_candidates + number_of_candidates // 2
    filtered_cars = estimate_car(car, number_of_retreived_cars)
    ranked = list(sorted(filtered_cars, key=lambda x: car_similarity_score(car, x), reverse=True))
    top_k = ranked[:number_of_candidates]
    return top_k


def get_price(car, list_of_cars):
    """
    Predicts price for a car
    :param car: car to predict price for
    :param list_of_cars: similar advertisements/training data
    :return: float
    """
    gbr = GradientBoostingRegressor(loss='ls', max_depth=6)
    X, y = build_train_data(list_of_cars)
    gbr.fit(X, y)
    X = np.array(get_features(car))

    return gbr.predict(X.reshape(1, len(X)))[0]


def build_train_data(list_of_cars):
    data = []
    prices = []
    for car in list_of_cars:
        data.append(get_features(car))
        prices.append(car.price)
    return data, prices


def get_features(car):
    year = datetime.datetime.now().year
    # features =['year_model', 'mileage', 'engine_type_diesel', 'engine_type_fuel', 'engine_type_gybrid',
    #           'engine_type_electric', 'kpp_automat', 'kpp_mechanic', 'kpp_variator', 'kpp_gybrib']
    # Бензин/Дизель/Гибрид/Электро
    # Механика/ Автомат/Робот /Вариатор
    return [year - car.year, car.km, car.engine_type.lower() == 'дизель', car.engine_type.lower() == 'бензин',
            car.engine_type.lower() == 'гибрид', car.engine_type.lower() == 'электро',
            car.kpp.lower() == 'автомат', car.kpp.lower() == 'механика', car.kpp.lower() == 'вариатор',
            car.kpp.lower() == 'гибрид']


def cars_to_json(cars: List[Car], best_price, ):
    """
    Method to pars cars array to json
    :param cars:List of cars more similar to query car
    :return: json string to send to server
    """
    answer = {}
    answer['bestprice'] = best_price
    best_variants = {}
    for i, car in enumerate(cars):
        car_dict = {}
        car_dict['id'] = i
        car_dict['Модель'] = car.model
        car_dict['Бренд'] = car.brand
        car_dict['Год'] = car.year
        car_dict['Двигатель'] = car.engine_type
        car_dict['Пробег'] = car.km
        car_dict['КПП'] = car.kpp
        car_dict['Цена'] = car.price
        best_variants[f'info{i}'] = car_dict
    answer['bestvariants'] = best_variants
    return json.dumps(answer)


def car_from_json(js: str):
    """
    TODO cast numeric params to int and
    Parses car info from json
    :param json:
    :return:
    """
    car = Car('', {})
    params = json.loads(js)
    category = params['category']
    if category != 'cars':
        return None
    car.brand = params.get('carbrand', '')
    car.model = params.get('cartype', '')
    car.year = params.get('year', 0)
    car.km = params.get('mileage', 0)
    car.engine_type = params.get('enginetype')
    car.engine_volume = params.get('evolume')
    car.kpp = params.get('korobkaa')
    return car

