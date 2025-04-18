from ib_insync import IB

def initialize_ibkr():
    ib = IB()
    ib.connect("127.0.0.1", 7497, clientId=1)  # TWS 또는 Gateway에 연결
    return ib
