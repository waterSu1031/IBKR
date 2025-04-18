from app.models.signal import Signal
from app.utils.order import create_order

class IBKRExecutor:
    def __init__(self, ib):
        self.ib = ib

    def execute(self, signal: Signal, price: float):
        contract = self._default_contract()

        if signal == Signal.BUY:
            order = create_order("BUY", 1)
        elif signal == Signal.SELL:
            order = create_order("SELL", 1)
        else:
            return None

        trade = self.ib.placeOrder(contract, order)
        self.ib.sleep(1)
        return trade

    def _default_contract(self):
        from ib_insync import Stock
        return Stock('AAPL', 'SMART', 'USD')  # 기본 테스트용 주식
