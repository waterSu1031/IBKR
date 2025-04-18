from app.utils.strategy import SimpleMovingAverageStrategy
from app.models.signal import Signal

def test_strategy():
    strategy = SimpleMovingAverageStrategy(short_window=3, long_window=5)
    test_data = [100, 102, 105, 104, 103, 108, 110, 112]

    for price in test_data:
        signal = strategy.generate_signal(price)
        print(f"Price: {price} => Signal: {signal}")
