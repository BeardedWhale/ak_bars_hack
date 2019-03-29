import abc
from abc import ABC


class BaseApi(ABC):
    def __init__(self, name, sleep_time: int):
        """
        Base class for api
        :param name: name of api
        :param sleep_time:  time between requests
        """
        self.name = name
        self.sleep_time = sleep_time

    @abc.abstractmethod
    def register_api(self):
        pass
