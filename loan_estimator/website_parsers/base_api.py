import abc
from abc import ABC
from datetime import timedelta


class BaseApi(ABC):
    def __init__(self, name, sleep_time: int):
        """
        Base class for api
        :param name: name of api
        :param sleep_time:  time between requests
        """
        self.name = name
        self.sleep_time = timedelta(seconds=sleep_time)

    @abc.abstractmethod
    def register_api(self):
        pass

    @abc.abstractmethod
    def send_auto_request(self, mark: str, model: str, engine: str = '', mileage: str = '',
                          gearbox: str = '', year: str = '', start_id: int = 0):
        pass
