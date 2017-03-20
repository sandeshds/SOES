from constants import constants


class Stock:
    def __init__(self, company):
        self.company = company
        self.current_stock_orders_to_sell = []
        self.current_stock_orders_to_buy = []

    def init_sell_order(self, stock_order):
        self.current_stock_orders_to_sell.append(stock_order)

    def init_buy_order(self, stock_order):
        self.current_stock_orders_to_buy.append(stock_order)

    def process_orders(self):
        for sell_order in self.current_stock_orders_to_sell:
            if sell_order.status != constants.STATUS_CLOSED:
                for buy_order in self.current_stock_orders_to_buy:
                    if buy_order.status != constants.STATUS_CLOSED:
                        self.__update_order_status(sell_order, buy_order)

    @staticmethod
    def __update_order_status(sell_order, buy_order):
        if sell_order.quantity - buy_order.quantity > 0:
            sell_order.quantity -= buy_order.quantity
            buy_order.quantity = 0
            buy_order.status = constants.STATUS_CLOSED
        elif sell_order.quantity - buy_order.quantity < 0:
            buy_order.quantity -= sell_order.quantity
            sell_order.quantity = 0
            sell_order.status = constants.STATUS_CLOSED
        else:
            buy_order.quantity = 0
            buy_order.status = constants.STATUS_CLOSED
            sell_order.quantity = 0
            sell_order.status = constants.STATUS_CLOSED
