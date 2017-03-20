from main.constants import constants
from main.parser.file_parser import FileParser
from model.stock_order import create_stock_orders_from_list
from processor.stock_processor import StockProcessor


class StockOrderExecutionSystem:
    def __init__(self, input_file_path):
        self.input_file_path = input_file_path

    def run(self):
        stock_list = FileParser(self.input_file_path).parse_file_and_get_list()
        stock_orders = create_stock_orders_from_list(stock_list)
        StockProcessor(stock_orders).process_orders()


def initialize_app():
    StockOrderExecutionSystem(constants.INPUT_FILE_PATH).run()
