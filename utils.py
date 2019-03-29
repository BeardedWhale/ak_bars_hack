from constants import *

def params_match(car, estimated_car):
    """ марка, год, модель, двигатель, пробег, год, статус(битая?),
        тип кузова, КПП, руль, мощность двигателя(лс) """
    assert(car.brand == estimated_car.brand)
    assert(car.model == estimated_car.model)
    
    # Engine type match: gasoline, diesel ...
    if car.engine_type != estimated_car.engine_type:
        return False
    
    # Engine volume difference in range
    if abs(car.engine_volume - estimated_car.engine_volume) > max_engine_vol_diff:
        return False
    
    # Year of production doesn't differ much
    if abs(car.year - estimated_car.year) > max_year_diff:
        return False

    # Kilometers run difference
    if abs(car.km - estimated_car.km) > max_km_diff:
        return False

    # Cars have same transmission
    if car.kpp != estimated_car.kpp:
        return False

    # Horse power doesn't differ much 
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


def car_similarity_score(car, other_car):
    score = 0
    if car.brand == other_car.brand:
        score += 0.2 
    if car.model == other_car.model:
        score += 0.2
    if car.engine_type == other_car.engine_type:
        score += 0.15
    if car.engine_volume == other_car.engine_type:
        score += 0.15
    if car.year == other_car.year:
        score += 0.15
    if car.kpp == other_car.kpp:
        score += 0.15
    return score
