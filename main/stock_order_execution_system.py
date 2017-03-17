from main.constants import constants
from main.parser.file_parser import FileParser


class StockOrderExecutionSystem:
    def __init__(self, input_file_path):
        self.input_file_path = input_file_path

    def run(self):
        stock_list = FileParser(self.input_file_path).parse_file_and_get_list()
        print(stock_list)


def initialize_app():
    StockOrderExecutionSystem(constants.INPUT_FILE_PATH).run()
