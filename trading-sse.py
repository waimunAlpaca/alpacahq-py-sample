from alpaca.trading.stream import TradingStream

ALPACA_API_KEY = ""
ALPACA_API_SECRET = ""

trading_stream = TradingStream(
    ALPACA_API_KEY,
    ALPACA_API_SECRET,
)


async def trades_update_handler(data):
    # trade updates will arrive in our async handler
    print("trade", data)


# subscribe to trade updates and supply the handler as a parameter
trading_stream.subscribe_trade_updates(trades_update_handler)

# start our websocket streaming
trading_stream.run()
