import requests
import logging
import time
import hmac
import hashlib
from urllib.parse import urlencode
from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = "https://testnet.binancefuture.com"
API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

if not API_KEY or not API_SECRET:
    raise ValueError("API credentials not found in .env")

def get_timestamp():
    return int(time.time() * 1000)

def generate_signature(secret, params):
    query_string = urlencode(params)
    return hmac.new(
        secret.encode(),
        query_string.encode(),
        hashlib.sha256
    ).hexdigest()

class BinanceFuturesClient:

    def __init__(self):
        self.headers = {"X-MBX-APIKEY": API_KEY}

    def place_order(self, symbol, side, order_type, quantity, price=None, stop_price=None):
        url = BASE_URL + "/fapi/v1/order"
        params = {
            "symbol": symbol.upper(),
            "side": side,
            "type": order_type,
            "quantity": quantity,
            "timestamp": get_timestamp()
        }

        if order_type == "LIMIT":
            if price is None:
                raise ValueError("LIMIT orders require price")
            params["price"] = price
            params["timeInForce"] = "GTC"

        if order_type == "STOP_MARKET":
            if stop_price is None:
                raise ValueError("STOP_MARKET requires stop_price")
            params["stopPrice"] = stop_price

        params["signature"] = generate_signature(API_SECRET, params)

        try:
            logging.info(f"REQUEST: {params}")
            response = requests.post(url, headers=self.headers, params=params, timeout=10)
            logging.info(f"RESPONSE: {response.text}")
            if response.status_code != 200:
                raise Exception(f"API Error: {response.text}")
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"API ERROR: {str(e)}")
            raise
