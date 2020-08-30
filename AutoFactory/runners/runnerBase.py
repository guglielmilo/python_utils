from abc import ABCMeta, abstractmethod
from typing import Callable

class RunnerBase(metaclass=ABCMeta):

    subclasses = {}

    def __init__(self, params : dict):
        self.params = params

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses[cls.name()] = cls

    @classmethod
    def create(cls, name: str, params : dict):

        if name not in cls.subclasses:
            raise NotImplementedError(name + ' runner not available')

        derived_class = cls.subclasses[name]
        return derived_class(params)

    @classmethod
    @abstractmethod
    def name(cls) -> str:
        raise NotImplementedError

    @abstractmethod
    def run(self, user_input: dict, user_params: dict):
        raise NotImplementedError
