from unittest import TestCase

from model.stock import Stock
from model.stock_order import StockOrder


class TestStock(TestCase):
    def test_should_process_orders(self):
        stock_order_one = StockOrder(1, 'Buy', 'abc', 5)
        stock_order_two = StockOrder(2, 'Buy', 'abc', 5)
        stock_order_three = StockOrder(3, 'Sell', 'abc', 10)
        stock_order_four = StockOrder(4, 'Sell', 'xyz', 10)
        stock = Stock('abc')

        stock.init_buy_order(stock_order_one)
        stock.init_buy_order(stock_order_two)
        stock.init_sell_order(stock_order_three)
        stock.init_sell_order(stock_order_four)
        stock.process_orders()

        self.assertTrue(stock_order_one.status == 'closed')
        self.assertTrue(stock_order_two.status == 'closed')
        self.assertTrue(stock_order_three.status == 'closed')
        self.assertTrue(stock_order_four.status == 'open')

        self.assertTrue(stock_order_one.quantity == 0)
        self.assertTrue(stock_order_two.quantity == 0)
        self.assertTrue(stock_order_three.quantity == 0)
        self.assertTrue(stock_order_four.quantity == 10)
