from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def parser_base(self):
        pass

class AbstractParser(ABC):
    @abstractmethod
    def parser_function(self):
        pass