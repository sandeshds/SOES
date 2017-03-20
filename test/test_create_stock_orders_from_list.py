from unittest import TestCase

from model.stock_order import create_stock_orders_from_list


class TestCreateStockOrdersFromList(TestCase):
    def test_create_stock_orders_from_list(self):
        stock_list = [[1221, 'sell', 'abc', 1]]
        stock_orders = create_stock_orders_from_list(stock_list)
        self.assertTrue(len(stock_orders) == 1)

    def test_should_skip_order_if_invalid_quantity(self):
        stock_list = [[1221, 'sell', 'abc', 1], [1222, 'sell', 'abc', '1as']]
        stock_orders = create_stock_orders_from_list(stock_list)
        self.assertTrue(len(stock_orders) == 1)
