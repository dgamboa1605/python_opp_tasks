from abc import ABC, abstractmethod


class BaseClass(ABC):

    @abstractmethod
    def calculate_length(self):
        raise NotImplementedError

    @abstractmethod
    def validate_input(self):
        raise NotImplementedError
