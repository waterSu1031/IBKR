import time
from app.utils.strategy import SimpleMovingAverageStrategy
from app.utils.trade_executor import IBKRExecutor
from app.utils.ibkr import initialize_ibkr
from app.models.signal import Signal

def run_live_loop():
    ib = initialize_ibkr()
    executor = IBKRExecutor(ib)
    strategy = SimpleMovingAverageStrategy()

    while True:
        data_point = strategy.fetch_market_data()
        signal = strategy.generate_signal(data_point)
        if signal and signal != Signal.NONE:
            executor.execute(signal, data_point)
        time.sleep(10)
