from alpaca.broker.client import (
    BrokerClient,
    GetEventsRequest,
)
from alpaca.broker.requests import ListAccountsRequest
from alpaca.broker.enums import AccountEntities
from datetime import datetime


ALPACA_API_KEY = ""
ALPACA_API_SECRET = ""

broker_client = BrokerClient(
    ALPACA_API_KEY,
    ALPACA_API_SECRET,
)

request_params = GetEventsRequest(
    since=datetime.strptime("2023-01-01", "%Y-%m-%d"),
)

# Get account status events
account_status_events = broker_client.get_account_status_events(filter=request_params)
for account_status in account_status_events:
    print("account_status", account_status)

# Get trade status events
trade_events = broker_client.get_trade_events(filter=request_params)
for trade in trade_events:
    print("trade", trade)

# Get journal status events
journal_events = broker_client.get_journal_events(filter=request_params)
for journal in journal_events:
    print("journal", journal)

# Get transfer status events
transfer_events = broker_client.get_transfer_events(filter=request_params)
for transfer in transfer_events:
    print("transfer", transfer)

# Get non_trading_activity status events
non_trading_activity_events = broker_client.get_non_trading_activity_events(
    filter=request_params
)
for non_trading_activity in non_trading_activity_events:
    print("non_trading_activity", non_trading_activity)
