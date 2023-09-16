from alpaca.data.live import StockDataStream
from alpaca.data.enums import DataFeed

ALPACA_API_KEY = ""
ALPACA_API_SECRET = ""

client = StockDataStream(
    ALPACA_API_KEY,
    ALPACA_API_SECRET,
    feed=DataFeed.IEX,
    # feed=DataFeed.SIP,
    # feed=DataFeed.OTC,
)


# Get quote
async def quote_data_handler(data):
    print("quote", data)


# Get trade
async def trade_data_handler(data):
    print("trade", data)


# Get trade
async def bar_data_handler(data):
    print("bar", data)


# Subscribe to quotes
client.subscribe_quotes(quote_data_handler, "SPY")

# Subscribe to trades
client.subscribe_trades(trade_data_handler, "SPY")

# Subscribe to bars
client.subscribe_bars(bar_data_handler, "SPY")

client.run()
