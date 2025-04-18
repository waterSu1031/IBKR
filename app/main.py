from fastapi import FastAPI
from app.routes.webhook import router as webhook_router

app = FastAPI(
    title="IBKR Auto-Trading Server",
    description="TradingView 신호 기반 IBKR 자동매매 시스템",
    version="1.0"
)

app.include_router(webhook_router, prefix="/webhook", tags=["Webhook"])
