# Trade algo

It's an algo to make cryptocurrency exchanges with a configuration in json and the use of matplotlib to observe the data.

## Lessons Learned

Learned a lot of information in trading, Python, api and learned Ichimoku.

## Run Locally

Clone the project

```bash
  git clone git@github.com:YannisDef/auto_buy_crypto.git
```

Go to the project directory

```bash
  cd auto_buy_crypto/
```

Run project

```bash
  ./run.sh
```

Run help

```bash
  ./run.sh -h
```

Run tests

```bash
  pytest
```

## JSON Configuration

He is located in data/value.json

It contains all the data to configure the bot and the graph

    "symbole": symbol of your exchange
    "interval": interval between request
    "Wallet": {
        "crypto_to_buy": crypto you bought
        "crypto_for_buy": the crypto you start with
    }
    "time_between_request": time between request with Binance
    "percent_to_buy": the percentages to sell from your wallet
    "percent_to_sell": the percentages to buy from your wallet
    "stop_to_buy": if your money in your wallet is lower than this value, the Bot will stop buying
    "sum_to_sell_min": the minimum you need before selling your crypto



    "name": graphics name
    "size_max": graphics size
    "xlabel": graphics xlabel
    "ylabel": graphics ylabel
    "pause": interval between update, need to be the same of "interval"
    "background_color": color of the background


## 🛠 Skills

Python, Matplotlib, API Binance, Ichimoku algorithm

## Authors

- [@YannisDef](https://github.com/YannisDef)
