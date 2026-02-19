from bot.orders import place_order
from bot.validators import validate_side, validate_order_type
from bot.logging_config import setup_logger
import logging

def main():
    setup_logger()
    print("=== Binance Futures Testnet Trading Bot ===\n")

    try:
        # Symbol
        symbol = input("Enter symbol (e.g., BTCUSDT): ").upper()

        # Side
        while True:
            side = input("Enter side (BUY/SELL): ").upper()
            try:
                side = validate_side(side)
                break
            except ValueError as e:
                print(f"❌ {e}")

        # Order Type
        while True:
            order_type = input("Enter order type (MARKET/LIMIT/STOP_MARKET): ").upper()
            try:
                order_type = validate_order_type(order_type)
                break
            except ValueError as e:
                print(f"❌ {e}")

        # Quantity
        while True:
            try:
                quantity = float(input("Enter quantity: "))
                if quantity <= 0:
                    raise ValueError("Quantity must be positive")
                break
            except ValueError as e:
                print(f"❌ {e}")

        # Price (for LIMIT)
        price = None
        if order_type == "LIMIT":
            while True:
                try:
                    price = float(input("Enter price for LIMIT order: "))
                    if price <= 0:
                        raise ValueError("Price must be positive")
                    break
                except ValueError as e:
                    print(f"❌ {e}")

        # Stop Price (for STOP_MARKET)
        stop_price = None
        if order_type == "STOP_MARKET":
            while True:
                try:
                    stop_price = float(input("Enter stop price for STOP_MARKET order: "))
                    if stop_price <= 0:
                        raise ValueError("Stop price must be positive")
                    break
                except ValueError as e:
                    print(f"❌ {e}")

        # Confirm Order
        print("\n===== ORDER SUMMARY =====")
        print(f"Symbol: {symbol}")
        print(f"Side: {side}")
        print(f"Type: {order_type}")
        print(f"Quantity: {quantity}")
        if price:
            print(f"Price: {price}")
        if stop_price:
            print(f"Stop Price: {stop_price}")

        confirm = input("Proceed with order? (Y/N): ").upper()
        if confirm != "Y":
            print("❌ Order cancelled by user")
            return

        # Place Order
        response = place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price,
            stop_price=stop_price
        )

        print("\n===== ORDER RESPONSE =====")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print(f"Avg Price: {response.get('avgPrice')}")
        print("\n✅ SUCCESS: Order placed successfully")

    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        logging.error(e)

if __name__ == "__main__":
    main()
