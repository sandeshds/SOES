from constants import constants


class StockOrder:
    def __init__(self, stock_id, side, company, quantity):
        self.quantity = int(quantity)
        self.quantity_requested = quantity
        self.company = company
        self.side = side
        self.stock_id = stock_id
        self.status = constants.STATUS_OPEN


def create_stock_orders_from_list(stock_list):
    stock_orders = []
    for stock in stock_list:
        new_stock_order = StockOrder(stock[0], stock[1], stock[2], stock[3])
        stock_orders.append(new_stock_order)
    return stock_orders

