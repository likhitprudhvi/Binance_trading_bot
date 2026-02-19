from bot.client import BinanceFuturesClient

client = BinanceFuturesClient()

def place_order(symbol, side, order_type, quantity, price=None, stop_price=None):
    return client.place_order(
        symbol=symbol,
        side=side,
        order_type=order_type,
        quantity=quantity,
        price=price,
        stop_price=stop_price
    )
