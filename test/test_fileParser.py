from unittest import TestCase


class TestFileParser(TestCase):
    def test_parse_file_and_get_list(self):
        from main.parser.file_parser import FileParser
        stock_list = FileParser('../Resources/Test_Input.csv').parse_file_and_get_list()
        self.assertEqual(stock_list[0], ['1', 'Buy', 'ABC', '10'])

