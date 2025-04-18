from app.utils.strategy import BaseStrategy
from app.utils.trade_executor import DummyExecutor
from app.models.signal import Signal

def run_backtest(strategy: BaseStrategy, historical_data: list):
    executor = DummyExecutor()
    for data_point in historical_data:
        signal = strategy.generate_signal(data_point)
        if signal and signal != Signal.NONE:
            executor.execute(signal, data_point)

    print("백테스트 종료")
