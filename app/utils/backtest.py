from app.utils.strategy import SimpleMovingAverageStrategy
from app.models.signal import Signal


def run_backtest(price_data):
    strategy = SimpleMovingAverageStrategy()

    results = []
    for price in price_data:
        signal = strategy.generate_signal(price)
        results.append((price, signal))

    return results
