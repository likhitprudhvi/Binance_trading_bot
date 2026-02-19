# Binance Futures Testnet Trading Bot

A Python trading bot for **Binance Futures Testnet (USDT-M)** supporting **MARKET**, **LIMIT**, and **STOP_MARKET** orders.  
Includes an **interactive CLI** for enhanced user experience and optional lightweight UI via Streamlit.

---

## Setup

1. **Clone the repository**:

```bash
git clone <your-repo-url>
cd trading_bot
Install dependencies:

pip install -r requirements.txt
Create a .env file with your Testnet API credentials:

BINANCE_API_KEY=your_api_key_here
BINANCE_API_SECRET=your_api_secret_here
⚠️ Do not commit .env to GitHub; it contains sensitive keys.

Optional: Install Streamlit for lightweight UI:

pip install streamlit
How to Run
Interactive CLI
python cli.py
Follow prompts for: symbol, side (BUY/SELL), order type (MARKET/LIMIT/STOP_MARKET), quantity, price (LIMIT), stop price (STOP_MARKET)

Confirm the order before submission

Streamlit UI (Optional)
streamlit run app.py
Fill in the form and click Place Order

Examples
MARKET Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
LIMIT Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 60000
STOP_MARKET Order
python cli.py --symbol BTCUSDT --side SELL --type STOP_MARKET --quantity 0.01 --stop_price 55000
Assumptions
Minimum order notional = 100 USDT (Binance requirement)

Only USDT-M Futures Testnet supported

Logging saved to bot.log in the project root

API keys stored in .env (never push to public GitHub)

Sample Logs
MARKET Order

2026-02-19 22:55:10,123 - INFO - REQUEST: {'symbol': 'BTCUSDT', 'side': 'BUY', 'type': 'MARKET', 'quantity': 0.01, 'timestamp': ..., 'signature': '...'}
2026-02-19 22:55:11,234 - INFO - RESPONSE: {"orderId":12345678,"status":"NEW","executedQty":"0","avgPrice":"0"}
LIMIT Order

2026-02-19 22:56:15,321 - INFO - REQUEST: {'symbol': 'BTCUSDT', 'side': 'SELL', 'type': 'LIMIT', 'quantity': 0.01, 'price': 60000, 'timeInForce': 'GTC', 'timestamp': ..., 'signature': '...'}
2026-02-19 22:56:16,432 - INFO - RESPONSE: {"orderId":12345679,"status":"NEW","executedQty":"0","avgPrice":"0"}
Requirements
requests
python-dotenv
streamlit  # optional for lightweight UI
Notes
Ensure system time is synced to avoid timestamp errors

Adjust quantity to meet the minimum notional requirement

Use Testnet for all testing to avoid real fund risk
