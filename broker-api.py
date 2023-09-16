from alpaca.broker.client import BrokerClient
from alpaca.broker.requests import ListAccountsRequest
from alpaca.broker.enums import AccountEntities
from datetime import datetime


ALPACA_API_KEY = ""
ALPACA_API_SECRET = ""

broker_client = BrokerClient(
    ALPACA_API_KEY,
    ALPACA_API_SECRET,
)

filter = ListAccountsRequest(
    created_after=datetime.strptime("2022-01-30", "%Y-%m-%d"),
    entities=[AccountEntities.CONTACT, AccountEntities.IDENTITY],
)

accounts = broker_client.list_accounts(search_parameters=filter)
print("accounts", accounts)
