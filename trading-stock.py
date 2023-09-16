from alpaca.trading.client import TradingClient
from alpaca.trading.requests import (
    MarketOrderRequest,
    LimitOrderRequest,
    GetAssetsRequest,
    GetOrdersRequest,
)
from alpaca.trading.enums import (
    OrderSide,
    TimeInForce,
    OrderType,
    AssetStatus,
    AssetClass,
    QueryOrderStatus,
)


ALPACA_API_KEY = ""
ALPACA_API_SECRET = ""

trading_client = TradingClient(
    ALPACA_API_KEY,
    ALPACA_API_SECRET,
)


active_us_equity_data = GetAssetsRequest(
    status=AssetStatus.ACTIVE,
    asset_class=AssetClass.US_EQUITY,
)
# Get the list of ACTIVE US_EQUITY
assets = trading_client.get_all_assets(filter=active_us_equity_data)
# print("assets", assets)


market_order_data = MarketOrderRequest(
    symbol="AAPL",
    qty=1,
    side=OrderSide.BUY,
    time_in_force=TimeInForce.DAY,
)
# Create Market order
# market_order = trading_client.submit_order(order_data=market_order_data)


limit_order_data = LimitOrderRequest(
    symbol="TSLA",
    qty=10,
    side=OrderSide.BUY,
    type=OrderType.LIMIT,
    time_in_force=TimeInForce.DAY,
    extended_hours=True,
    limit_price=200,
)
# Create Limit order
# limit_order = trading_client.submit_order(order_data=limit_order_data)


request_params = GetOrdersRequest(
    status=QueryOrderStatus.OPEN,
)
# Get the list of OPEN orders
open_orders = trading_client.get_orders(filter=request_params)
print("open_orders", open_orders)

# Gets all the current open positions
positions = trading_client.get_all_positions()
print("positions", positions)

# Get account details
account = trading_client.get_account()
print("account", account)
