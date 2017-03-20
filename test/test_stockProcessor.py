from unittest import TestCase

from model.stock_order import StockOrder
from processor.stock_processor import StockProcessor


class TestStockProcessor(TestCase):

    def test_should_process_stock_orders_and_create_object_map(self):
        stock_order_one = StockOrder(1, 'Buy', 'abc', 5)
        stock_order_two = StockOrder(2, 'Sell', 'abc', 5)
        stock_order_three = StockOrder(3, 'Buy', 'xyz', 5)
        stock_order_four = StockOrder(4, 'Sell', 'xyz', 5)
        stock_processor = StockProcessor([stock_order_one, stock_order_two, stock_order_three, stock_order_four])
        stock_processor.process_orders()
        self.assertTrue('xyz' in list(stock_processor.map_of_stock_and_orders.keys()))
        self.assertTrue('abc' in list(stock_processor.map_of_stock_and_orders.keys()))

    def test_should_process_stock_orders(self):
        stock_order_one = StockOrder(1, 'Buy', 'abc', 5)
        stock_order_two = StockOrder(2, 'Sell', 'abc', 5)
        stock_order_three = StockOrder(3, 'Buy', 'xyz', 5)
        stock_order_four = StockOrder(4, 'Sell', 'xyz', 5)
        stock_processor = StockProcessor([stock_order_one, stock_order_two, stock_order_three, stock_order_four])
        stock_processor.process_orders()

        self.assertTrue(stock_order_one.status == 'closed')
        self.assertTrue(stock_order_two.status == 'closed')
        self.assertTrue(stock_order_three.status == 'closed')
        self.assertTrue(stock_order_four.status == 'closed')

        self.assertTrue(stock_order_one.quantity == 0)
        self.assertTrue(stock_order_two.quantity == 0)
        self.assertTrue(stock_order_three.quantity == 0)
        self.assertTrue(stock_order_four.quantity == 0)
