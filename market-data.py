from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import (
    StockBarsRequest,
    StockTradesRequest,
    StockLatestTradeRequest,
    StockLatestQuoteRequest,
)

from alpaca.data.enums import (
    Adjustment,
    DataFeed,
)

from datetime import datetime
from alpaca.data.timeframe import TimeFrame

ALPACA_API_KEY = ""
ALPACA_API_SECRET = ""

client = StockHistoricalDataClient(
    ALPACA_API_KEY,
    ALPACA_API_SECRET,
)


multisymbol_latest_quote_request_params = StockLatestQuoteRequest(
    symbol_or_symbols=["SPY", "AAPL", "TSLA"]
)
latest_multisymbol_quotes = client.get_stock_latest_quote(
    multisymbol_latest_quote_request_params
)
print("latest_multisymbol_quotes", latest_multisymbol_quotes)


multisymbol_stock_bar_request_params = StockBarsRequest(
    symbol_or_symbols=["AAPL", "TSLA"],
    adjustment=Adjustment.ALL,
    feed=DataFeed.IEX,
    timeframe=TimeFrame.Minute,
    start=datetime.strptime("2023-01-03", "%Y-%m-%d"),
    end=datetime.strptime("2023-01-04", "%Y-%m-%d"),
)
latest_multisymbol_bars = client.get_stock_bars(multisymbol_stock_bar_request_params)
print("latest_multisymbol_bars", latest_multisymbol_bars)


multisymbol_stock_trade_request_params = StockTradesRequest(
    symbol_or_symbols=["AAPL", "TSLA"],
    feed=DataFeed.IEX,
    start=datetime.strptime("2023-01-03", "%Y-%m-%d"),
    end=datetime.strptime("2023-01-04", "%Y-%m-%d"),
)
latest_multisymbol_trades = client.get_stock_trades(
    multisymbol_stock_trade_request_params
)
print("latest_multisymbol_trades", latest_multisymbol_trades)
