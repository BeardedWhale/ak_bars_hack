import abc
from abc import ABC
from typing import Dict
from constants import ADS_API
from constants import CRWL_API

class Item(ABC):
    def __init__(self, api_name, json: Dict):
        if api_name == ADS_API:
            # self.init_ads(json)
            self.params = json.get('self.params', {})
            if not self.params:
                self.params = {}
            self.id = json.get("id", '')  # Идентификатор записи
            self.url = json.get("url", '')  # Url объявления на сайте-источнике
            self.title = json.get("title", '')  # Заголовок
            self.price = json.get("price", '')  # Цена
            self.time = json.get("time", '')  # Дата и время добавления объявления в нашу систему, либо время обновления. Время московское
            self.nedvigimost_type_id = json.get("nedvigimost_type_id", '')  # ID типа недвижимости: 1 - Продам, 2 - Сдам, 3 - Куплю или 4 - Сниму
            self.avitoid = json.get('avitoid', '')  # ID объявления на сайте-источнике
            self.source_id = json.get("source_id", '')  # ID cайта-источника в нашей системе
            self.params = json.get("self.params", '')  # Дополнительные параметры объявления
            self.cat1_id = json.get("cat1_id", '')  # ID категории первого уровня, например, категория Недвижимость имеет значение 1
            self.cat2_id = json.get("cat2_id", '')  # ID категории второго уровня, например, категория Квартиры имеет значение 2
            self.cat1 = json.get('cat1', '')  # Название категории первого уровня, например, Недвижимость
            self.cat2 = json.get("cat2", '')  # Название категории второго уровня, например, Квартиры


class Car(Item):
    def __init__(self, api_name, json):
        super().__init__(api_name, json)
        if api_name == ADS_API:
            self.init_ads()

    def init_ads(self):
        self.engine_type = self.params.get("Тип двигателя", '')  #Бензин, Дизель, Гибрид или Электро
        self.engine_volume = self.params.get("Объём двигателя, л", '')
        self.status = self.params.get("Состояние", '')
        #self.km = self.params.get("Пробег, км", '')
        self.brand = self.params.get("Марка", '')
        self.model = self.params.get("Модель", '')
        self.corpus_type = self.params.get("Тип кузова", '')
        self.kpp = self.params.get("Коробка передач", '')
        self.circle = self.params.get("Руль", '') #левый / правый
        self.year = self.params.get("Год выпуска", '0')
        self.engine_horse_power = self.params.get("Мощность двигателя, л.с.", '')
        self.color = self.params.get("Цвет", '')
        self.owners = self.params.get("Владельцев по ПТС", -1)
        self.wd = self.params.get("Привод", '')
        self.auto_type = self.params.get("Тип автомобиля", '')
        self.number_of_doors = self.params.get("Количество дверей", '0')

    def init_crwl(self, json):
        self.dt = json.get("dt", '')
        self.url = json.get("url", '') # ссылка
        self.engine_type = json.get("fuel", '')  # Бензин, Дизель, Гибрид или Электро
        self.engine_volume = json.get("enginevol", '')
        self.status = json.get("condition", '')  # битый / не битый
        self.run = json.get("run", '')  # пробег
        self.run_ed = json.get("run_ed", '')  # единица измерения пробега
        self.brand = json("marka", '')
        self.model = json.get("модель", '')
        self.corpus_type = self.params.get("body", '')
        self.kpp = json.get("transmission", '')
        self.circle = json.get("wheel", '')  # левый / правый
        self.year = json.get("year", '')
        self.engine_horse_power = json.get("horse", '')
        self.color = json.get("color", '')
        self.owners = json.get("pts_owner", -1)
        self.wd = json.get("drive", '')
        self.price = json.get("price", '')


class House(Item):
    def __init__(self, api_name, json):
        super().__init__(api_name, json)
        self.region = json.get('region', '')  # Только название региона
        self.city1 = json.get('city1', '')  # Только название города
        self.metro = json.get('metro', '')  # Метро или район


class Commercial_house(House): #catid = 7
    def __init__(self, api_name, json):
        super().__init__(api_name, json)
        self.type = self.params.get('Вид объекта', '') #Гостиница, Офисное помещение, Помещение свободного назначения, Производственное помещение, Складское помещение, Торговое помещение
        self.area = self.params.get('Площадь', '')
        self.floor = self.params.get('Этаж', '')
        self.floors_in_house = self.params.get('Этажность здания', '')


class Flat(House): #catid = 2
    def __init__(self, api_name, json):
        super().__init__(api_name, json)
        self.number_of_rooms = self.params.get('Количество комнат', '') #Студия / 1 / 2 / ... / >9
        self.house_type = self.params.get('Вид объекта', '') #Вторичка / Новостройка
        self.house_type = self.params.get('Тип дома', '') #Кирпичный / Панельный / Блочный / Монолитный / Деревянный
        self.floor = self.params.get('Этаж', '')
        self.number_of_floors = self.params.get('Этажей в доме', '')
        self.flat_area = self.params.get('Площадь', '')
        self.kitchen_area = self.params.get('Площадь кухни', '')
        self.living_area = self.params.get('Жилая площадь', '')


class Room(House):  # catid = 3
    def __init__(self, api_name, json):
        super().__init__(api_name, json)
        self.rooms_in_flat = self.params.get('Комнат в квартире', '')  # 1 / 2 / ... / >9
        self.house_type = self.params.get('Тип дома', '')  # Кирпичный / Панельный / Блочный / Монолитный / Деревянный
        self.floor = self.params.get('Этаж', '')
        self.number_of_floors = self.params.get('Этажей в доме', '')
        self.room_area = self.params.get('Площадь комнаты', '')


class Living_house(House): # catid = 4
    def __init__(self, api_name, json):
        super().__init__(api_name, json)
        self.house_type = self.params.get('Вид объекта', '') # Дом / Дача / Коттедж / Таунхаус
        self.number_of_floors = self.params.get('Этажей в доме', '')
        self.wall_material = self.params.get('Материал стен', '')
        self.house_area = self.params.get('Площадь дома', '')
        self.land_area = self.params.get('Площадь участка', '')
        self.distance_to_city = self.params.get('Расстояние до города', '')

