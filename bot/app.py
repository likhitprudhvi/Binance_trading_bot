import streamlit as st
from bot.orders import place_order
from bot.validators import validate_side, validate_order_type

st.title("Binance Futures Testnet Trading Bot")

symbol = st.text_input("Symbol", "BTCUSDT")
side = st.selectbox("Side", ["BUY", "SELL"])
order_type = st.selectbox("Order Type", ["MARKET", "LIMIT", "STOP_MARKET"])
quantity = st.number_input("Quantity", min_value=0.0001, value=0.01, step=0.001)
price = st.number_input("Price (for LIMIT)", value=0.0)
stop_price = st.number_input("Stop Price (for STOP_MARKET)", value=0.0)

if st.button("Place Order"):
    try:
        response = place_order(
            symbol=symbol,
            side=validate_side(side),
            order_type=validate_order_type(order_type),
            quantity=quantity,
            price=price if price > 0 else None,
            stop_price=stop_price if stop_price > 0 else None
        )
        st.success(f"Order Placed! ID: {response.get('orderId')}")
        st.json(response)
    except Exception as e:
        st.error(f"Error: {e}")
