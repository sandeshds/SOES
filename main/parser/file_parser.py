import csv


class FileParser:
    def __init__(self, input_file_path):
        self.input_file_path = input_file_path

    def parse_file_and_get_list(self):
        with open(self.input_file_path, 'rt') as csv_file:
            stock_list = list(csv.reader(csv_file, delimiter=',', quotechar='|'))
            return stock_list
