from alpaca.data.live import CryptoDataStream

ALPACA_API_KEY = ""
ALPACA_API_SECRET = ""

client = CryptoDataStream(
    ALPACA_API_KEY,
    ALPACA_API_SECRET,
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
client.subscribe_quotes(
    quote_data_handler,
    "DOGE/USD",
    "DOGE/USDC",
    "DOGE/USDT",
)

# Subscribe to trades
client.subscribe_trades(
    trade_data_handler,
    "ETH/BTC",
    "ETH/USD",
    "ETH/USDC",
    "ETH/USDT",
    "BTC/USD",
    "BTC/USDC",
    "BTC/USDT",
    "BCH/BTC",
    "BCH/USD",
    "BCH/USDC",
    "BCH/USDT",
    "USDC/USD",
    "USDT/USD",
    "USDT/USDC",
)

# Subscribe to bars
client.subscribe_bars(
    bar_data_handler,
    "SHIB/USD",
    "SHIB/USDC",
    "SHIB/USDT",
    "SUSHI/USD",
    "SUSHI/USDC",
    "SUSHI/USDT",
)

client.run()
