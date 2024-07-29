from AbstractParser.Abstract_parser import AbstractParser
from Parser_scripts.rawabi_parser import rawabi_parser


class RawabiConcreateParser(AbstractParser):
    def parser_function(self):
        return rawabi_parser()

