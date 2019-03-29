import abc
from abc import ABC
from typing import Dict


class Item(ABC):
    def __init__(self, json: Dict):
        self.id = json.get("id", '')  # Идентификатор записи
        self.url = json.get("url", '')  # Url объявления на сайте-источнике
        self.title = json.get("title", '')  # Заголовок
        self.price = json.get("price", '')  # Цена
        self.time = json.get("time", '')# Дата и время добавления объявления в нашу систему, либо время обновления. Время московское
        self.nedvigimost_type_id = json.get("nedvigimost_type_id", '')  # ID типа недвижимости: 1 - Продам, 2 - Сдам, 3 - Куплю или 4 - Сниму
        self.avitoid = json.json['avitoid']  # ID объявления на сайте-источнике
        self.source_id = json.get("source_id", '') # ID cайта-источника в нашей системе
        self.params = json.get("params", '') # Дополнительные параметры объявления
        self.cat1_id = json.get("cat1_id", '') # ID категории первого уровня, например, категория Недвижимость имеет значение 1
        self.cat2_id = json.get("cat2_id", '') # ID категории второго уровня, например, категория Квартиры имеет значение 2
        self.cat1 = json.get('cat1', '') # Название категории первого уровня, например, Недвижимость
        self.cat2 = json.get("cat2", '')# Название категории второго уровня, например, Квартиры
        self.param_xxx = json.get("param_xxx", '') # Дополнительный параметр с кодом xxx, коды параметров смотрите в разделе Параметры всех категорий


class Car(Item):
    def __init__(self, json):
        super().__init__(json)
        self.engine_type = json.get("params", {}).get("Тип двигателя", '') #Бензин, Дизель, Гибрид или Электро
        self.engine_volume = json.get("params", {}).get("Объём двигателя, л", '')
        self.status = json.get("params", {}).get("Состояние", '')
        #self.km = json.get("params", {}).get("Пробег, км", '')
        self.brand = json.get("params", {}).get("Мартка", '')
        self.model = json.get("params", {}).get("Модель", '')
        self.corpus_type = json.get("params", {}).get("Тип кузова", '')
        self.kpp = json.get("params", {}).get("Коробка передач", '')
        self.circle = json.get("params", {}).get("Руль", '') #левый / правый
        self.year = json.get("params", {}).get("Год выпуска", '')
        self.engine_horse_power = json.get("params", {}).get("Мощность двигателя, л.с.", '')
        self.color = json.get("params", {}).get("Цвет", '')
        self.owners = json.get("params", {}).get("Владельцев по ПТС", -1)
        self.wd = json.get("params", {}).get("Привод", '')
        self.auto_type = json.get("params", {}).get("Тип автомобиля", '')
        self.number_of_doors = json.get("params", {}).get("Количество дверей", '')


class House(Item):
    def __init__(self, json):
        super().__init__(json)
        self.region = json['region']  # Только название региона
        self.city1 = json['city1']  # Только название города
        self.metro = json['Тип обх']  # Метро или район


class Commercial_house(House): #catid = 7
    def __init__(self, json):
        super().__init__(json)
        self.type = json.get("params", {}).get('Вид объекта', '') #Гостиница, Офисное помещение, Помещение свободного назначения, Производственное помещение, Складское помещение, Торговое помещение
        self.area = json.get("params", {}).get('Площадь', '')
        self.floor = json.get("params", {}).get('Этаж', '')
        self.floors_in_house = json.get("params", {}).get('Этажность здания', '')


class Flat(House): #catid = 2
    def __init__(self, json):
        super().__init__(json)
        self.number_of_rooms = json.get("params", {}).get('Количество комнат', '') #Студия / 1 / 2 / ... / >9
        self.house_type = json.get("params", {}).get('Вид объекта', '') #Вторичка / Новостройка
        self.house_type = json.get("params", {}).get('Тип дома', '') #Кирпичный / Панельный / Блочный / Монолитный / Деревянный
        self.floor = json.get("params", {}).get('Этаж', '')
        self.number_of_floors = json.get("params", {}).get('Этажей в доме', '')
        self.flat_area = json.get("params", {}).get('Площадь', '')
        self.kitchen_area = json.get("params", {}).get('Площадь кухни', '')
        self.living_area = json.get("params", {}).get('Жилая площадь', '')


class Room(House):  # catid = 3
    def __init__(self, json):
        super().__init__(json)
        self.rooms_in_flat = json.get("params", {}).get('Комнат в квартире', '')  # 1 / 2 / ... / >9
        self.house_type = json.get("params", {}).get('Тип дома', '')  # Кирпичный / Панельный / Блочный / Монолитный / Деревянный
        self.floor = json.get("params", {}).get('Этаж', '')
        self.number_of_floors = json.get("params", {}).get('Этажей в доме', '')
        self.room_area = json.get("params", {}).get('Площадь комнаты', '')


class Living_house(House): # catid = 4
    def __init__(self, json):
        super().__init__(json)
        self.house_type = json.get("params", {}).get('Вид объекта', '') # Дом / Дача / Коттедж / Таунхаус
        self.number_of_floors = json.get("params", {}).get('Этажей в доме', '')
        self.wall_material = json.get("params", {}).get('Материал стен', '')
        self.house_area = json.get("params", {}).get('Площадь дома', '')
        self.land_area = json.get("params", {}).get('Площадь участка', '')
        self.distance_to_city = json.get("params", {}).get('Расстояние до города', '')

