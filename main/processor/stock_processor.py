from model.stock import Stock
from constants import constants
import csv


class StockProcessor:
    def __init__(self, stock_orders):
        self.stock_orders = stock_orders
        self.map_of_stock_and_orders = {}

    def process_orders(self):
        self.__create_stocks_for_companies(self.__get_list_of_companies())
        for stock_order in self.stock_orders:
            if stock_order.side == constants.STOCK_SELL:
                self.map_of_stock_and_orders[stock_order.company].init_sell_order(stock_order)
            elif stock_order.side == constants.STOCK_BUY:
                self.map_of_stock_and_orders[stock_order.company].init_buy_order(stock_order)
            else:
                print("Invalid Input, skipping the stock order")
                pass
            self.map_of_stock_and_orders[stock_order.company].process_orders()
        self.__print_output_to_csv()

    def __print_output_to_csv(self):
        with open('../Resources/output.csv', 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for stock_order in self.stock_orders:
                writer.writerow([stock_order.stock_id, stock_order.side, stock_order.company,
                                    stock_order.quantity_requested,
                                    stock_order.quantity, stock_order.status])

    def __get_list_of_companies(self):
        return list(set([o.company for o in self.stock_orders]))

    def __create_stocks_for_companies(self, companies):
        for company in companies:
            self.map_of_stock_and_orders[company] = Stock(company)
