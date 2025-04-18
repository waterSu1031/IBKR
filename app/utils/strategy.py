from collections import deque
from app.models.signal import Signal

class SimpleMovingAverageStrategy:
    def __init__(self, short_window=5, long_window=20):
        self.short_window = short_window
        self.long_window = long_window
        self.short_prices = deque(maxlen=short_window)
        self.long_prices = deque(maxlen=long_window)

    def generate_signal(self, price: float) -> Signal:
        self.short_prices.append(price)
        self.long_prices.append(price)

        if len(self.short_prices) < self.short_window or len(self.long_prices) < self.long_window:
            return Signal.NONE

        short_avg = sum(self.short_prices) / len(self.short_prices)
        long_avg = sum(self.long_prices) / len(self.long_prices)

        if short_avg > long_avg:
            return Signal.BUY
        elif short_avg < long_avg:
            return Signal.SELL
        return Signal.HOLD
