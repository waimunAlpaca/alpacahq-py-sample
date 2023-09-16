# alpacahq-py-sample

This repository provide an example for interacting with the API products that are offered by Alpaca. 

These API products are provided as various REST, WebSocket and SSE endpoints that allow you to do everything from streaming market data to creating your own investment apps.

## Getting Started

These instructions will get you a copy of the Broker API, Trading API & Market Data API up and running on your local machine for development and testing purposes. 

This example is built using [alpaca-py](https://github.com/alpacahq/alpaca-py), more examples can also be found in the [documentation](https://alpaca.markets/docs/python-sdk/index.html) website.

### Prerequisites

You need Python 3.7+ and to install [alpaca-py](https://github.com/alpacahq/alpaca-py).

```
pip install alpaca-py
```

### Running Broker API

A step by step series of examples to get the Broker API  development env running:

```
python broker-api.py
```

To get sse accounts, trade, journal, transfer and nta events updates:

```
python broker-sse.py
```

### Running Trading API

A step by step series of examples to place a market order, limit order and list the no. of open orders and positions, etc. 

```
python trading-stock.py
```

To get sse trade events updates:

```
python trading-sse.py
```

### Running Market Data Stream

A step by step series of examples to Market Data API & Web Sockets running.

To get historical bars, trades and the latest quotes:

```
python market-data.py
```

To subscribe to the latest quote, trade and bar:

```
python stream-stock.py
```

To subscribe to the latest news:

```
python wss-news.py
```

## Built With

* [README.md](https://github.com/waimunAlpaca/README.md) - Yet another README.md template! 

## Contributing

Want to file a bug, contribute some code, or improve documentation? Excellent! Read up on our [CONTRIBUTING.md](https://github.com/angular/angular/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Wai Mun** - *Initial work* - [waimunAlpaca](https://github.com/waimunAlpaca)

## License

This project is licensed under the Apache License License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* [CONTRIBUTING.md](https://github.com/angular/angular/blob/master/CONTRIBUTING.md) - Contributing to Angular.
* [Conventional Commits](https://www.conventionalcommits.org/) - A specification for adding human and machine readable meaning to commit messages.