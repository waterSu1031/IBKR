from ib_insync import IB
from app.utils.ibkr import initialize_ibkr

class Broker:
    def __init__(self):
        self.ib = initialize_ibkr()

    def place_market_order(self, contract, action, quantity):
        from ib_insync import MarketOrder
        order = MarketOrder(action, quantity)
        trade = self.ib.placeOrder(contract, order)
        self.ib.sleep(1)
        return trade
