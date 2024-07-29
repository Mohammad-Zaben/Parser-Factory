from AbstractParser.Abstract_parser import AbstractFactory
from Concreate_parsers.Concreate_parser import RawabiConcreateParser


class RawabiConcreateFactory(AbstractFactory):
    def parser_base(self):
        return RawabiConcreateParser()
