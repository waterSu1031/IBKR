import os
from dotenv import load_dotenv

load_dotenv()

IB_GATEWAY_HOST = os.getenv("IB_GATEWAY_HOST", "127.0.0.1")
IB_GATEWAY_PORT = int(os.getenv("IB_GATEWAY_PORT", 7497))
IB_CLIENT_ID = int(os.getenv("IB_CLIENT_ID", 1))
