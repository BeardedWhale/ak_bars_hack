import abc
from abc import ABC
from typing import Dict


class Item(ABC):
    def __init__(self, json: Dict):
        self.id = json['id']  # Идентификатор записи
        self.url = json['url']  # Url объявления на сайте-источнике
        self.title = json['title']  # Заголовок
        self.price = json['price']  # Цена
        self.time = json[
            'time']  # Дата и время добавления объявления в нашу систему, либо время обновления. Время московское
        self.phone = json['phone']  # Телефон
        self.phone_operator = json['phone_operator']  # Название мобильного оператора
        self.person = json['person']  # Персона для контактов, автор объявления
        self.contactname = json[
            'contactname']  # Контактное лицо. В основном бывает указано, если поле person содержит имя какой-нибудь компании.
        self.person_type = json[
            'person_type']  # Тип персоны для контактов. "Частное лицо", "Агентство" или "Частное лицо (фильтр)"
        self.person_type_id = json[
            'person_type_id']  # ID типа персоны для контактов. 1 - "Частное лицо", 2 - "Агентство" или 3 - "Частное лицо (фильтр)"
        self.city = json['city']  # Регион и Город вместе, для получения отдельных значений смотрите поля region и city1
        self.metro = json['metro']  # Метро или район
        self.address = json['address']  # Адрес
        self.description = json['description']  # Описание объявления
        self.nedvigimost_type = json['nedvigimost_type']  # Тип недвижимости: Продам, Сдам, Куплю или Сниму
        self.nedvigimost_type_id = json[
            'nedvigimost_type_id']  # ID типа недвижимости: 1 - Продам, 2 - Сдам, 3 - Куплю или 4 - Сниму
        self.avitoid = json['avitoid']  # ID объявления на сайте-источнике
        self.source = json['source']  # Сайт-источник
        self.source_id = json['source_id']  # ID cайта-источника в нашей системе
        self.images = json['images']  # Картинки. Массив объектов, каждый из которых имеет поле imgurl - адрес картинки
        self.params = json['params']  # Дополнительные параметры объявления
        self.cat1_id = json['cat1_id']  # ID категории первого уровня, например, категория Недвижимость имеет значение 1
        self.cat2_id = json['cat2_id']  # ID категории второго уровня, например, категория Квартиры имеет значение 2
        self.cat1 = json['cat1']  # Название категории первого уровня, например, Недвижимость
        self.cat2 = json['cat2']  # Название категории второго уровня, например, Квартиры
        self.coords = json['coords']  # Объект, содержащий координаты объявления, поля lat и lng
        self.region = json['region']  # Только название региона
        self.city1 = json['city1']  # Только название города
        self.param_xxx = json[
            'param_xxx']  # Дополнительный параметр с кодом xxx, коды параметров смотрите в разделе Параметры всех категорий
        self.count_ads_same_phone = json[
            'count_ads_same_phone']  # Количество объявлений с тем же номером. Имеет значение только для категории Недвижимость и подкатегорий, для других равно null.
        self.phone_protected = json[
            'count_ads_same_phone']  # Показывает, защищен ли телефон, актуально для объявлений с avito и realty.yandex.ru, для других источников равно null.

    @abc.abstractmethod
    def get_adverts_from_ads_api(self):
        pass


class Car(Item):
    def __init__(self, json):
        super().__init__(json)

# class House(Item):
#
