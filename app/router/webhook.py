from fastapi import APIRouter, Request
from app.utils.trade_executor import IBKRExecutor
from app.utils.ibkr import initialize_ibkr
from app.models.signal import Signal

router = APIRouter()


@router.post("/webhook")
async def webhook_handler(request: Request):
    payload = await request.json()
    signal = payload.get("signal")
    price = payload.get("price", 0)

    ib = initialize_ibkr()
    executor = IBKRExecutor(ib)

    if signal == "BUY":
        executor.execute(Signal.BUY, price)
    elif signal == "SELL":
        executor.execute(Signal.SELL, price)

    return {"status": "received"}
