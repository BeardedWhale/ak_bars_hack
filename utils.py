import re
from typing import List

from Item import Car
from constants import *
from website_parsers.ads_api.ads_api import ADS_API

ads_api = ADS_API()

def params_match(car, estimated_car):
    """ марка, год, модель, двигатель, пробег, год, статус(битая?),
        тип кузова, КПП, руль, мощность двигателя(лс) """
    # assert(car.brand == estimated_car.brand)
    # assert(car.model == estimated_car.model)=
    car_engine_type = car.engine_type.replace(' ', '')
    if car.brand != estimated_car.brand:
        return False
    if car.model != estimated_car.model:
        return False
    # Engine type match: gasoline, diesel ...
    if estimated_car.engine_type:
        if car_engine_type != estimated_car.engine_type:
            return False

    # Engine volume difference in range
    if estimated_car.engine_volume:
        if abs(car.engine_volume - estimated_car.engine_volume) > max_engine_vol_diff:
            return False

    # Year of production doesn't differ much
    if estimated_car.year:
        if abs(car.year - estimated_car.year) > max_year_diff:
            return False

    # Kilometers run difference
    # if estimated_car.km:
    #     if abs(car.km - estimated_car.km) > max_km_diff:
    #         return False

    # Cars have same transmission
    if estimated_car.kpp:
        if car.kpp != estimated_car.kpp:
            return False

    # Horse power doesn't differ much
    if estimated_car.engine_horse_power:
        if abs(car.engine_horse_power - estimated_car.engine_horse_power) > max_engine_hp_diff:
            return False

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
        cars, last_id = ads_api.send_auto_request(estimated_car.brand, estimated_car.model, start_id=start_id)
        if start_id and cars:
            if tried_once_more:
                cars.pop(0) # remove first element as we already retrieved it
            elif len(cars)==1:
                tried_once_more = True
        if not cars:
            break
        filtered = filter(cars, estimated_car)
        retrieved_cars.extend(filtered)
        start_id = last_id
    return retrieved_cars




def car_similarity_score(car, other_car)-> int:
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


def get_cars_candidates(car:Car, number_of_candidates: int)->List[Car]:

    number_of_retreived_cars = number_of_candidates + number_of_candidates//2
    filtered_cars = estimate_car(car, number_of_retreived_cars)
    ranked = list(sorted(filtered_cars, key=lambda x: car_similarity_score(car, x), reverse=True))
    top_k = ranked[:number_of_candidates]
    return top_k


