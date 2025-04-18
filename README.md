# IBKR 자동매매 서버 (Python + FastAPI + ib_insync)

이 프로젝트는 Interactive Brokers (IBKR) API와 FastAPI, ib_insync를 기반으로 주식 및 선물에 대한 자동매매 시스템을 구축하는 예제입니다.

## 기능 요약
- TradingView Webhook 신호 수신 및 자동 주문
- 실시간 가격에 기반한 전략 실행
- 모듈화된 구조로 종목, 전략 확장 가능

## 실행 방법

1. `.env` 파일 설정
2. 패키지 설치: `pip install -r requirements.txt`
3. FastAPI 서버 실행: `uvicorn main:app --reload`
4. IBKR TWS 또는 Gateway 실행 및 로그인

## 폴더 구조
