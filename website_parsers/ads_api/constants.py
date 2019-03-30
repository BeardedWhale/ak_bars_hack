CATEGORIES = {'Недвижимость': '1', 'Квартиры': '2', 'Комнаты': '3', 'Дома, дачи, коттеджи': '4',
              'Земельные участки': '5', 'Гаражи и машиноместа': '6', 'Коммерческая недвижимость': '7',
              'Недвижимость за рубежом': '8', 'Работа': '9', 'Вакансии': '10', 'Резюме': '11', 'Услуги': '12',
              'Предложения услуг': '13', 'Запросы на услуги': '14', 'Транспорт': '21', 'Автомобили': '22',
              'Мотоциклы и мототехника': '23', 'Грузовики и спецтехника': '24', 'Водный транспорт': '25',
              'Запчасти и аксессуары': '26', 'Для дома и дачи': '27', 'Бытовая техника': '28',
              'Мебель и интерьер': '29', 'Посуда и товары для кухни': '30', 'Продукты питания': '31',
              'Ремонт и строительство': '32', 'Растения': '33', 'Бытовая электроника': '34', 'Аудио и видео': '35',
              'Игры, приставки и программы': '36', 'Настольные компьютеры': '37', 'Ноутбуки': '38',
              'Оргтехника и расходники': '39', 'Планшеты и электронные книги': '40', 'Телефоны': '41',
              'Товары для компьютера': '42', 'Фототехника': '43', 'Хобби и отдых': '44', 'Билеты и путешествия': '45',
              'Велосипеды': '46', 'Книги и журналы': '47', 'Коллекционирование': '48', 'Музыкальные инструменты': '49',
              'Охота и рыбалка': '50', 'Спорт и отдых': '51', 'Животные': '52', 'Собаки': '53', 'Кошки': '54',
              'Птицы': '55', 'Аквариум': '56', 'Другие животные': '57', 'Товары для животных': '58',
              'Для бизнеса': '59', 'Готовый бизнес': '60', 'Оборудование для бизнеса': '61'}

REAL_ESTATE_CATEGORIES = {'Квартиры': 'Flat',
                          'Комнаты': 'Room',
                          'Дома, дачи, коттеджи': 'House',
                          'Коммерческая недвижимость': 'Commercial_house'}


class ADSResponseCode():
    """
    Class for ADS Response codes
    """
    SUCCESS = 200
    MISSING_PARAMETER = 400
    WRONG_USER_TOKEN = 401
    TOKEN_EXPIRED = 402
    USER_BLOCKED = 403
    NOT_FOUND = 404  # advert not found
    LIMIT_EXPIRED = 429  # wait 5 sec
    NOT_ENOUGH_RIGHTS = 452  # access only for partners program
    RESTRICTED_TO_REAL_ESTATE = 453
    RESTRICTED_TO_CITY = 454
